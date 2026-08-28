---
title: LLMs Can Design Near-Optimal OR Algorithms
title_zh: 大语言模型可设计接近最优的运筹学算法
authors:
- Jackie Baek
affiliations:
- New York University Stern School of Business
arxiv_id: '2608.27296'
url: https://arxiv.org/abs/2608.27296
pdf_url: https://arxiv.org/pdf/2608.27296
published: '2026-08-27'
collected: '2026-08-28'
category: LLM
direction: LLM 运筹学算法自动设计
tags:
- LLM
- Operations_Research
- Algorithm_Design
- Inventory_Optimization
- Assortment_Optimization
- Queueing_Scheduling
one_liner: 前沿LLM通过无调优单查询加Python沙箱，生成比肩甚至超越现有最优方法的运筹学算法
practical_value: '- 电商选品（assortment优化）、库存控制、履约调度等经典运筹场景，可直接复用「无调优prompt+Python沙箱」的协议，让LLM生成定制化算法，替代传统人工设计启发式、调参RL的长周期流程，快速拿到基线方案

  - 业务场景优先用Level2模式：针对固定问题大类（比如本店铺的选品优化）调用一次LLM生成通用算法，单次查询成本低，生成的算法是可解释代码，方便调试、合规校验，性能接近单实例定制方案

  - 前沿LLM的算法设计能力迭代极快（8个月内发布的模型性能差可达70%以上），业务侧可定期测试新模型在内部运筹问题上的表现，快速迭代决策方案拿收益'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
运筹学（OR）算法是电商库存管控、商品选品、履约调度、广告流量分配等核心场景的决策底座，传统OR算法需要领域专家针对问题结构定制开发，研发周期长、人力成本高；近年LLM已展现出代码生成、复杂数学问题求解能力，但其在标准化OR问题上的算法设计能力边界尚未得到系统验证，落地价值不明确。
### 方法关键点
- 定义两级LLM调用范式：Level1输入单个问题实例的具体参数，直接输出该实例的解；Level2仅输入问题大类的定义与参数范围，输出可复用的通用算法（输入任意实例参数即可输出对应解）
- 采用极简实验协议：仅给LLM提供无调优的问题描述prompt，搭配Python沙箱（仅支持标准库、numpy、scipy，无第三方商用求解器），不提供任何算法思路提示
- 测试4款8个月内发布的前沿大模型，覆盖OpenAI GPT-5系列、Anthropic Claude系列
### 关键实验结果
实验覆盖库存控制、排队网络调度、选品优化3类经典OR场景，共34个库存实例、13个排队网络实例、3393个选品优化实例，对比baseline包括DP精确解、人工调优的最优启发式算法、SOTA RL方法。最强模型gpt-5.6-sol在10个问题子类中，8个类的平均表现不逊于现有最优方法，6个类的所有实例表现持平或更优；Level2生成的通用算法性能接近Level1单实例求解，仅在嵌套Logit选品场景平均收益低1.2%。
### 核心结论
在数学定义明确的运筹学问题上，前沿LLM已经可以作为算法设计的核心基线，大幅降低定制化OR算法的研发门槛。
