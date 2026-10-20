---
title: 'MEMORA: A Memory-Enhanced Multimodal Committee Reranking Agent for Reasoning-Intensive
  Retrieval'
title_zh: MEMORA：面向推理密集型检索的记忆增强多模态重排序Agent
authors:
- Mohamed Mahmoud
- Mostafa Farouk Senussi
- Mahmoud Abdalla
- Mahmoud SalahEldin Kasem
- Abdelrahman Abdallah
- Hyun Soo Kang
affiliations:
- Chungbuk National University
- University of Innsbruck
arxiv_id: '2610.25282'
url: https://arxiv.org/abs/2610.25282
pdf_url: https://arxiv.org/pdf/2610.25282
published: '2026-10-18'
collected: '2026-10-20'
category: Agent
direction: 检索Agent · 多模态推理密集型检索
tags:
- Retrieval Agent
- Multimodal Retrieval
- Reranking
- Episodic Memory
- Chain-of-Thought
one_liner: 提出融合记忆模块、委员会重排、推理感知检索器的多模态检索Agent，大幅提升复杂检索效果
practical_value: '- 电商多模态搜索重排可借鉴因子委员会思路：将用户拍图+文字的query拆解为款式、价格、材质等独立意图因子，分别匹配打分后综合排序，替代单模型重排，提升复杂query匹配精度

  - 推理感知召回器训练trick可复用：用CoT标注的query+hard negative微调第一阶段召回模型，推理阶段无需额外输入即可捕获用户深层意图，适合解决长尾复杂query召回不足问题

  - 情景记忆模块可直接迁移到垂类检索：沉淀域内历史query的有效因子权重，无需重新训练模型即可动态适配域内query分布，尤其适合3C、美妆等专业度高的垂类搜索场景

  - 落地成本控制可参考性价比平衡点：设置3个意图因子可拿到87%的最大效果收益，仅付出44%的推理成本，平衡效果与LLM API开销'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有推理密集型多模态检索存在三大痛点：单体重排器无法适配异构查询意图、无状态检索丢弃历史策略经验、多模态编码器缺乏跨模态推理能力，甚至出现加入视觉信息后效果下降的反常识结果，无法满足带图、截图等复杂查询的检索需求。
### 方法关键点
- 推理感知稠密检索器：基于Qwen-Embedding，用2万+带CoT标注的Stack Exchange问答对+hard negative做InfoNCE微调，训练时输入CoT+查询，推理时仅输入原始查询即可捕获深层意图，无需额外视觉输入就超过专用多模态检索器效果
- 情景记忆模块：按域存储历史查询的因子分解、效果等信息，检索相似历史经验生成因子优先级先验，动态调整当前查询的因子权重，无需重训即可适配域内分布
- 协同因子委员会重排：将查询拆解为多个意图因子，生成因子专属子查询扩展召回池，构建因子-文档证据二部图，综合因子支持度、覆盖率、最低分等信号打分，可选调用记忆感知元判决模型生成最终排序
- 自适应控制器：根据排序裕度、内存命中率等信号动态决定是否扩展召回、调用判决模型或停止，平衡效果和计算开销
### 关键结果
在MM-BRIGHT基准29个域上测试，文本到文本检索nDCG@10达41.5，超最优文本Agent基线+8.3；多模态查询到文本检索nDCG@10达38.9，超最优多模态Agent基线+7.9。消融实验显示因子证据图与打分贡献最大，情景记忆对多模态任务增益更显著。

最值得记住的一句话：多模态复杂检索的核心不是直接编码视觉信号，而是将视觉内容转换为可推理的结构化因子，结合历史经验做分层决策，效果远好于端到端单模型
