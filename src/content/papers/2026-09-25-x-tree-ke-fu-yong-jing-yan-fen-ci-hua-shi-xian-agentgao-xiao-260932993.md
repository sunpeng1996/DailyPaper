---
title: 'X-Tree: Tokenizing Reusable Experience for Efficient Agent Generalization'
title_zh: X-Tree：可复用经验分词化实现Agent高效泛化
authors:
- Sitao Cheng
- Xunjian Yin
- Zhiyuan Sun
- Yuxuan Li
- Ruiwen Zhou
- Xiangru Jian
- Victor Zhong
affiliations:
- University of Waterloo
- Duke University
- National University of Singapore
arxiv_id: '2609.32993'
url: https://arxiv.org/abs/2609.32993
pdf_url: https://arxiv.org/pdf/2609.32993
published: '2026-09-25'
collected: '2026-10-03'
category: Agent
direction: Agent训练 · 可复用经验结构化挖掘
tags:
- Agent_Training
- Skill_Mining
- RL
- Experience_Reuse
- OPSD
one_liner: 零LLM调用从Agent轨迹中挖掘可复用技能树X-Tree，三种集成方案大幅提升训练效率与泛化性
practical_value: '- 电商导购Agent、流程型交互Agent可直接复用X-Tree的经验挖掘逻辑，无需LLM调用即可从历史成功交互轨迹中提取高频复用的操作路径（如筛选→加购→结算流程），挖掘成本极低

  - 无仿真环境的离线Agent训练场景，可将X-Tree节点作为独立训练实例，配合步匹配+深度缩放的奖励设计，解决长序列轨迹奖励稀疏、数据利用率低的问题，适合复杂推荐路径、客服流程优化等业务

  - 在线RL冷启动阶段验证信号稀疏时，可引入X-Tree的自适应技能bonus作为中间奖励，无需额外训练过程奖励模型即可加快训练收敛，泛化性优于纯结果导向的RL

  - OPSD自蒸馏场景中可用X-Tree完全替代LLM生成的技能库作为自教师的特权上下文，零大模型调用成本即可达到与LLM生成技能相当的效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent训练将交互轨迹作为平token序列处理，均匀分配训练权重，忽略跨任务复用的子流程结构，稀缺轨迹数据的利用率极低；过往技能抽象方案依赖LLM调用生成自然语言技能，成本高且技能仅存在于prompt层面，无法内化到模型权重，泛化性局限于检索场景。

### 方法关键点
1. 动作规范化：将原始动作映射为`verb<role>`形式的统一token，剥离具体参数噪声，凸显结构复用性
2. X-Score打分：结合动作对的复用频率、长度、成功episode占比三个维度计算可复用性得分，递归合并高得分动作对生成X-Tree，全程零LLM调用，每个节点对应一个可复用的组合技能
3. 三种训练集成方案：
   - 离线RL：将X-Tree每个节点作为独立训练实例，优化目标包含步匹配奖励+深度缩放的节点完成奖励
   - 在线RLVR：新增自适应技能bonus，奖励权重随验证信号丰富度自动衰减，冷启动阶段提供有效梯度
   - OPSD自蒸馏：X-Tree作为自教师的特权上下文，替代LLM生成的技能库

### 关键实验
在WebArena、ScienceWorld、WebShop三个主流Agent环境，1.5B/3B/7B三个模型尺度下验证：离线RL方案比全量SFT基准高4.5% SR；在线RLVR方案比纯结果导向GRPO最高提升5.8% SR、4.6% WebShop分级得分；OPSD场景下X-Tree效果与GPT生成的技能库完全相当，零LLM调用成本。

### 核心结论
有限Agent训练经验下，结构化复用高频成功技能是提升数据利用率与泛化性的核心路径，无需LLM介入的X-Tree可最大化挖掘存量轨迹数据的价值
