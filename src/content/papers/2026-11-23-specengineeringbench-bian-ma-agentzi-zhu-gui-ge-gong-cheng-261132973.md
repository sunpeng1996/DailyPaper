---
title: 'SpecEngineeringBench: Evaluating Coding Agents as Autonomous Specification
  Engineers'
title_zh: SpecEngineeringBench：编码Agent自主规格工程能力评估基准
authors:
- Xingjian Wang
- Shijian Wang
- Minghao Liu
- Ji Zou
- Zetao Yang
- Xinping Lei
- Yiming Liang
- Shen Yan
- Enduo Zhao
- Xiaoyang Shen
affiliations:
- TokenWave AI
- Independent Researcher
- The University of Tokyo
- Monolith Management, US
arxiv_id: '2611.32973'
url: https://arxiv.org/abs/2611.32973
pdf_url: https://arxiv.org/pdf/2611.32973
published: '2026-11-23'
collected: '2026-11-25'
category: Agent
direction: 编码Agent · 能力评估基准
tags:
- CodingAgent
- Benchmark
- TestGeneration
- DefectDetection
- LLMEvaluation
one_liner: 构建跨16类场景的编码Agent自主规格工程能力评估基准，填补无提示缺陷挖掘能力评估空白
practical_value: '- 做业务Agent（如电商系统迭代自动化测试Agent、推荐策略效果核验Agent）能力评估时，可参考该基准「表面指标与核心业务目标解耦」的评估思路，避免高覆盖/高通过率下实际业务价值不足的问题

  - 开发自动化测试类Agent时，可复用基准中「自主生成测试用例→执行分析→缺陷定位」的两阶段架构，减少人工指定测试入口、测试范围的成本

  - 上线Agent前需增加无额外提示的真实场景测试项，避免仅在完备提示下测得的效果和上线后实际表现出现大幅落差'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有编码Agent评估基准普遍提供问题描述、指定测试入口等人工提示，未覆盖Agent自主判断测试对象、定位缺陷的能力，无法反映真实场景下将需求转化为可执行测试、主动挖掘未知缺陷的规格工程能力。
### 方法关键点
- 基准包含78个开源Python仓库的100个实例，覆盖16个应用类别，每个实例内置多个已标注缺陷
- 设置测试集生成、执行分析挖掘缺陷两个互补任务，从测试有效性、缺陷检测、覆盖率、定位精度召回多维度评估
### 关键结果
7个前沿编码Agent测试中，91.47%首过通过率、80.48%变更聚焦覆盖率下，缺陷修复通过率仅26.36%；定位召回率从文件级78.11%降至函数级51.29%；自主测试生成比仅依赖存量测试集的文件/函数/代码块定位召回率分别提升4.99/2.77/2.69pp
