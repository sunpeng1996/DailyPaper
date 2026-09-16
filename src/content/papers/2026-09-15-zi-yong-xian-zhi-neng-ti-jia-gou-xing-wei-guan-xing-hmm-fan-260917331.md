---
title: Self-Emergence Agent Architecture:Behavior-Inertia HMM, Reflexive Metacognition,and
  Social-Contrastive Self-Modeling
title_zh: 自涌现智能体架构：行为惯性HMM、反思元认知与社会对比自建模
authors:
- Xiaoyang Liu
affiliations:
- Independent Researcher
arxiv_id: '2609.17331'
url: https://arxiv.org/abs/2609.17331
pdf_url: https://arxiv.org/pdf/2609.17331
published: '2026-09-15'
collected: '2026-09-16'
category: Agent
direction: 智能体自进化 多智能体社会自涌现
tags:
- LLM Agent
- HMM
- Metacognition
- Multi-Agent
- Self-Emergence
one_liner: 提出无预设人格的自涌现智能体架构，通过惯性-反思-社会闭环实现稳定个性分化
practical_value: '- 电商用户建模可复用HMM编码行为惯性的思路，将用户长期消费/浏览偏好编码为可更新的状态转移矩阵，替代单纯的兴趣向量，减少用户兴趣漂移，提升长周期推荐一致性

  - 个性化导购/客服Agent可落地「反思→参数更新」闭环，将每轮对话后的反思结果直接调整Agent服务人设的转移参数，而非仅存入RAG，实现长期稳定的个性化服务人设

  - 多智能体仿真推荐策略时，可引入社会对比分化机制，让初始同质的模拟用户自发分化出不同消费决策人格，更真实复现用户群体决策分布，降低推荐策略冷启动的仿真偏差'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前LLM Agent存在三大结构性缺陷：人格随输入prompt漂移、反思仅作为文本存储无法改变底层行为倾向、无内生自我-他人边界，现有生成式智能体依赖预设静态人设与记忆，无法实现连续内生的自我演化，无法支撑个性化长期智能体与大规模多智能体社会仿真需求。

### 方法关键点
- 行为惯性模块：将长期行为/认知偏好编码为HMM可编辑状态转移矩阵，作为人格的数学载体
- 反思元认知模块：将自然语言反思解析为转移矩阵的增量更新，直接修改行为倾向而非仅存储于记忆
- 社会对比模块：初始完全同质的多智能体在交互中持续对比自身与他人行为，自发形成自我-他人边界
- 闭环逻辑：社会行动→反馈→自我反思→惯性参数更新→差异化行为，构成完整自涌现循环

### 关键结果
对比baseline为仅将反思存储为文本的Reflexion式架构：
1. 30种子无LLM机制原型实验：SEAA组智能体HMM转移矩阵两两Frobenius距离从0.03升至1.91，自我模型两两距离达0.51，人格确定性（1-归一化熵）达0.84，对照组所有指标无显著变化
2. DeepSeek-Chat真实LLM实验：SEAA组自访谈文本两两Jaccard相似度仅0.267，远低于对照组的0.391；5智能体讨论自发形成共识枢纽与一致排斥的边缘人社会结构，对照组无稳定角色分化

### 核心洞见
不要只把反思存在记忆里，让反思直接更新底层行为参数，才能实现真正的长期内生演化
