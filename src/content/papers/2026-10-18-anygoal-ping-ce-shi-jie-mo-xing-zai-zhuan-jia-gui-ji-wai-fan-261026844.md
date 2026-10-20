---
title: 'AnyGoal: On World Model Generalization Beyond Expert Rollouts'
title_zh: AnyGoal：评测世界模型在专家轨迹外泛化能力的基准
authors:
- Heejeong Nam
- Divyat Mahajan
- Quentin Le Lidec
- Randall Balestriero
- David Klindt
affiliations:
- Brown University
- Cold Spring Harbor Laboratory
- Mila, Université de Montréal
- New York University
arxiv_id: '2610.26844'
url: https://arxiv.org/abs/2610.26844
pdf_url: https://arxiv.org/pdf/2610.26844
published: '2026-10-18'
collected: '2026-10-20'
category: Agent
direction: Agent 世界模型泛化能力评测
tags:
- World Model
- Compositional Generalization
- Benchmark
- Agent Planning
- OOD Evaluation
one_liner: 提出AnyGoal评测基准，验证当前世界模型在目标偏移任务下的组合泛化失效问题
practical_value: '- 训练面向业务决策的Agent/世界模型时，不能仅验证分布内指标，需增加组合泛化校验，避免模型学到专家行为shortcut而非可复用的决策逻辑，可应用于用户浏览路径规划、个性化任务引导等场景

  - 可复用AnyGoal的「边际分布校验+联合覆盖度评估」方法，用于业务OOD场景的模型效果前置验证：只要新场景的单个特征/动作都在训练覆盖范围内，即可快速评估模型的组合泛化性能，无需额外采集大量新场景数据

  - 若业务场景属于低交互的自由决策类（如内容推荐的浏览路径规划），现有世界模型泛化性较好；若属于高交互的关键转化类（如下单、付费路径引导），需额外增加交互机制的结构化约束提升泛化能力'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有世界模型的评测大多局限于专家轨迹的分布内任务，无法验证模型是否真正学到可复用的环境动力学，而非拟合训练数据的行为相关性；实际Agent规划需要应对大量未见过的目标任务，缺乏系统的组合泛化评测框架来衡量世界模型的真实泛化能力。
### 方法关键点
- 定义组合泛化评测范式：测试集所有状态、动作的边际分布均在训练覆盖范围内，仅状态-动作的组合方式未在训练数据中出现，排除了未见因子的干扰
- 构建AnyGoal开源基准：基于4个主流世界模型环境衍生8个目标偏移任务，支持标准化的轨迹预测和MPC规划效果评测
- 配套三层校验机制：范围校验、马氏距离校验、KDE密度校验保证测试集符合组合泛化设定，同时设计动作敏感度指标诊断模型是否学到行为shortcut
### 关键实验结果
测试了LeWM、DINO-WM、DriftWorld等6类主流世界模型，结果显示所有模型在目标偏移任务上均出现显著性能下降：接触丰富的任务规划成功率最高下降81.4%，预测误差最高提升3个数量级；即使提供Oracle状态输入，接触类任务的泛化失败率仍超过70%。
### 核心结论
世界模型的泛化能力无法仅靠数据规模扩张解决，需要针对动力学机制识别和组合泛化做架构或训练目标的特殊设计
