---
title: Agent Priors-guided Policy Learning
title_zh: Agent先验引导的策略学习（APPL）框架
authors:
- Puming Jiang
- Tianrun Hu
- Haozhe Du
- Yibo Li
- Zhiwei Xue
- Xinhu Li
- Harold Soh
affiliations:
- National University of Singapore
arxiv_id: '2609.35690'
url: https://arxiv.org/abs/2609.35690
pdf_url: https://arxiv.org/pdf/2609.35690
published: '2026-09-27'
collected: '2026-10-02'
category: Agent
direction: Agent 策略学习与技能组合优化
tags:
- Agent
- Structural Prior
- Skill Composition
- Policy Learning
- OOD Generalization
one_liner: 将技能训练的结构先验作为组合接口，同时提升小样本下的技能泛化与任务组合泛化性能
practical_value: '- 建设Agent技能库时，可给每个工具/技能附加训练结构先验、适用范围、验证结果作为元数据，而非仅提供名称/功能描述，帮助上层调度Agent精准选择技能，降低切换失败率，可直接复用在电商导购Agent、多策略推荐调度等场景

  - 小样本训练业务策略时，可同时生成多种不同结构先验的策略版本保留备选，线上根据场景特征动态选择最优策略，比单一定制策略的泛化性更好，适用于冷启动推荐、小流量新场景策略落地

  - 技能分割时保留相邻技能的重叠过渡样本训练，可提升技能切换时的稳定性，可复用在多轮对话推荐的话术衔接、长流程用户引导的节点切换等场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有技能学习与任务组合架构存在信息断层：上层调度Agent仅通过名称、指令等抽象描述调用技能，无法获知技能训练时的结构假设与实际适用范围，小样本演示场景下难以同时兼顾技能OOD泛化与组合泛化，跨技能切换失败率高。

### 方法关键点
- 离线阶段由construction agent将完整演示分割为带重叠过渡区的可复用技能，为每个技能生成多种结构先验（如物体相对坐标系、局部TCP修正等）的Diffusion Policy，训练验证后为每个策略附加先验描述、切换条件、训练支持范围、验证结果作为接口元数据，形成冻结技能库。
- 线上runtime agent无需更新权重，仅根据当前状态、任务目标读取接口元数据，动态选择最优策略、设置调用参数与停止条件，组合完成未见过的新任务。

### 关键实验结果
在MetaWorld 6个操作任务、ManiSkill 5个长周期任务上验证：
- 仅2条演示时，MetaWorld任务OOD技能泛化成功率达89.6%，是固定关系先验策略的2.36倍；
- ManiSkill长任务物体位置偏移场景下成功率达50.0%，是全任务Diffusion Policy的5倍，任务级变体成功率92.5%，可解决8/16未见过的技能组合；
- 隐藏接口元数据后，组合成功率下降75%，验证了先验接口的核心价值。

### 核心结论
用于塑造策略训练泛化性的结构先验，同样可以作为上层Agent调度技能的可靠接口信息，打通训练与推理的信息壁垒能显著提升系统整体泛化能力。
