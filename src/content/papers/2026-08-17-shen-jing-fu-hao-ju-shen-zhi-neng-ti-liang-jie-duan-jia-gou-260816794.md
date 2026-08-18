---
title: Neurosymbolic Embodied Agents
title_zh: 神经符号具身智能体：两阶段架构实现高可靠长序列任务规划
authors:
- Mohammad Albinhassan
- Yuming Feng
- Alessandra Russo
- Pranava Madhyastha
affiliations:
- Imperial College London
- Johns Hopkins University
- City, University of London
arxiv_id: '2608.16794'
url: https://arxiv.org/abs/2608.16794
pdf_url: https://arxiv.org/pdf/2608.16794
published: '2026-08-17'
collected: '2026-08-18'
category: Agent
direction: 具身Agent · 神经符号规划
tags:
- Embodied Agent
- Neurosymbolic
- PDDL
- Constrained Decoding
- MCTS
- VLM
one_liner: 解耦视觉探索与符号规划，通过约束解码+MCTS生成可执行计划，小模型性能远超大模型直出策略
practical_value: '- 电商导购/任务型Agent可复用两阶段架构：先做目标导向的信息采集（用户需求、场景约束），再做受约束的规划生成，避免动作幻觉，可靠性远高于纯端到端大模型，同时降低推理成本

  - 推荐/广告多步运营路径规划可借鉴约束解码+MCTS思路：把业务规则（合规要求、用户偏好约束）做成动态token掩码，解码时直接屏蔽无效选项，再用MCTS选择长期最优路径，效果远好于纯Prompt工程

  - 低算力场景的Agent/推荐系统可参考小模型优化思路：引入明确的外部结构约束（状态转移逻辑、业务规则），可大幅降低对模型参数规模的依赖，4B模型效果超过27B直出的结论可直接复用'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有VLM/LLM驱动的具身Agent直接生成动作序列时，容易违反环境动态、出现grounding错误，长horizon任务下错误累积，成功率极低；纯端到端策略依赖极大模型规模，推理和交互成本极高，且无法保证计划可执行。

### 方法关键点
- 两阶段解耦架构：Phase I 探索阶段，VLM搭配探索控制器，仅采集和目标相关的视觉谓词、实例绑定，生成符号化初始状态，避免全场景重构的资源浪费；Phase II 利用阶段，基于PDDL转移模型做状态依赖的约束解码，每一步仅保留符合当前状态动作前置条件的token，从根源避免生成不可执行动作
- 搭配token级MCTS，用领域无关的规划启发式函数评估可执行计划的长期收益，平衡LLM的先验偏好和全局目标达成性

### 关键结果
在VirtualHome、ALFWorld两个 household 任务benchmark测试：4B-27B参数的模型用该架构，VirtualHome成功率94.5%~99.5%，ALFWorld成功率90.3%~97.8%；4B模型比27B直接VLM策略分别高32、63.4个百分点；生成token比扩展思考少4倍，模型可见图像比直接交互少5.6倍；消融实验显示约束和MCTS单独用在ALFWorld成功率都不足1/3，结合后超过95%。

**最值得记住的一句话：明确的结构约束可以替代大量的模型参数规模，把感知和规划解耦、把动作合法性从模型需要推断的知识变成解码时强制满足的不变量，是提升Agent可靠性、降低成本的核心路径**
