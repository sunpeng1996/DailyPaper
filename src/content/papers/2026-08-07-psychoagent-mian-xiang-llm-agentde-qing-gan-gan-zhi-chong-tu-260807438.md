---
title: 'PsychoAgent: An Affect-Sensitive Cognitive Architecture for Conflict-Aware
  Memory in LLM Agents'
title_zh: PsychoAgent：面向LLM Agent的情感感知冲突感知记忆认知架构
authors:
- Mohammad Amanlou
- Parham Abed Azad
- Farbod Davoodi
- Mostafa Masumi
- Behnam Bahrak
- Abdol-Hossein Vahabie
affiliations:
- University of Tehran
- Sharif University of Technology
- Missouri University of Science and Technology
- Tehran Institute for Advanced Studies
- Khatam University
arxiv_id: '2608.07438'
url: https://arxiv.org/abs/2608.07438
pdf_url: https://arxiv.org/pdf/2608.07438
published: '2026-08-07'
collected: '2026-08-10'
category: Agent
direction: LLM Agent 情感感知记忆架构优化
tags:
- LLM Agent
- Affective Memory
- Cognitive Architecture
- RAG
- Conflict Monitoring
one_liner: 提出事实/情感双内存+冲突感知执行控制器的LLM Agent架构，大幅提升冲突场景关键记忆召回率
practical_value: '- 电商客服、纠纷调解类Agent可复用双内存检索思路：先做语义初筛保证相关性，再按业务自定义的「用户不满权重/历史投诉标签」重排序，既不跑偏又能命中高价值记忆，避免忽略用户情绪导致矛盾升级

  - 长期用户运营类Agent可借鉴离线记忆重组机制：定期聚合近期交互记忆、用户情感状态生成临时trace，模拟人类记忆整理逻辑，减少记忆冗余同时保留用户核心偏好与情感倾向

  - 高风险冲突场景的Agent可参考冲突关键记忆标注方法，预先定义高优先级记忆标签，定向优化召回策略，提升响应的场景适配性'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM Agent的记忆召回仅依赖语义相似度、时效性等指标，容易忽略语义不匹配但情感意义、冲突关联性极强的记忆，无法支撑类人的冲突场景决策，比如客服对话中忽略用户过往被伤害的情感记忆导致回复不当，因此需要构建融合情感与事实记忆的冲突感知Agent架构。

### 方法关键点
- 双内存设计：每个事件同时存储事实记忆、带[0,1] salience权重的情感记忆两条关联trace
- 分层检索：事实记忆直接取TopK语义匹配结果；情感记忆先取Top30语义候选，再按salience权重重排序取Top10，既保证相关性又优先高情感权重记忆
- 冲突感知执行控制器：融合上下文、双内存召回结果、当前情感状态、persona约束生成响应，支持离线每日重组近期记忆生成临时trace，模拟人类记忆整合

### 关键结果
在3个手动构造的冲突场景（家庭财务矛盾、职场创意剽窃、友谊背叛）下，对比语义-情感双内存无重排序消融、单内存RAG两个基线：关键冲突记忆召回率0.933 vs 0.500 vs 0.667，仅带来0.011的语义相似度损失；5名盲测评分者的标准化得分显示，PsychoAgent整体得分+0.22SD优于基线，虽无统计显著性但表现出明显优势。

**最值得记住的一句话**：情感感知记忆检索无需牺牲过多语义相关性，即可大幅提升冲突场景下关键记忆的召回效率，是构建类人行为Agent的可行路径。
