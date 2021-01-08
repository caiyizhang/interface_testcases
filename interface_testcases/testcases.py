#!/usr/bin/env python
# -*-coding:utf-8 -*-


'''
 ~ 接口多参数测试用例生成

'''


from typing import List
import random

from allpairspy import AllPairs


class InterfaceTestcases(object):
    """接口多参数测试用例生成"""

    def __init__(self, params: List) -> None:
        self.params = params
        self.normal_list = [row[0] for row in self.params]
        self.normal_cases = self.createPairs()

    def createPairs(self):
        ''' 生成正常测试用例 '''
        return [row + ['normal'] for row in AllPairs(self.normal_list)]

    def getRandomNormalCaseWithoutExcptParam(self, param_id: int) -> List:
        ''' 随机生成不包括异常参数的正常用例
            params: param_id：异常参数序号
            return: 不包括异常参数的随机正常用例
        '''
        case = self.normal_list[:param_id] + self.normal_list[param_id+1:]
        return [random.choice(row) for row in case]

    def createExceptionCases(self) -> List:
        ''' 生成异常测试用例 '''

        cases = []
        for i, exception_row in enumerate(self.params):
            exception_list = exception_row[1]
            for data in exception_list:
                new_case = self.getRandomNormalCaseWithoutExcptParam(i)
                new_case.insert(i, data)
                new_case.append('abnormal')
                cases.append(new_case)
        return cases

    def createNoParamsCases(self) -> List:
        ''' 获取不传参数的用例。
            1、每个必选参数生成一个不带该参数的用例
            2、所有非必选参数，生成一个不带所有必选参数的用例
        '''

        cases = []
        is_has_option_param = False

        # 可选参数用例，case要深度拷贝，否则后面可能改变normal_cases的值
        optional_param_cace = random.choice(self.normal_cases)[:]

        for i, row in enumerate(self.params):
            if row[-1]:

                # new_case要深度拷贝，否则会改变normal_cases的值
                new_case = random.choice(self.normal_cases)[:]
                new_case[i] = 'no_param'
                new_case[-1] = 'abnormal'
                cases.append(new_case)
            else:
                is_has_option_param = True
                optional_param_cace[i] = 'no_param'
        return cases + [optional_param_cace] if is_has_option_param else cases


if __name__ == "__main__":
    row = [1, 2, 3, 4, 5, 6]
    # print(random.choice(row))
    # print(row.insert(0, 0))
    # print(row)

    params = [
        [[1, 2], [0, 3], False],
        [[-1, -2], [0, -3], True],
        [[-3, 3], [-2, 4], False]
    ]
    cases = InterfaceTestcases(params)
    print(cases.createExceptionCases())
    print(cases.createPairs())
    # print(cases.getParamsRequiredInfo()[True])
    print(cases.getNoParamsCases())