---
title: 'Beyond the Vote: When Do LLMs Add Value to Retrieval-Based Tabular Classification?'
title_zh: 超越投票：检索式表格分类中LLM的增益适用场景研究
authors:
- Ziquan Wang
- Yuxuan Nie
- Jian Ma
- Yingjie Li
affiliations:
- 北京航空航天大学杭州国际创新研究院
- 北京大学
arxiv_id: '2610.29520'
url: https://arxiv.org/abs/2610.29520
pdf_url: https://arxiv.org/pdf/2610.29520
published: '2026-10-21'
collected: '2026-10-22'
category: Eval
direction: LLM性能评估 · 检索式表格分类
tags:
- LLM
- In-Context-Learning
- Retrieval-Augmented
- Tabular-Classification
- KNN
one_liner: 在相同检索样本下对比LLM与距离加权KNN，明确检索式表格分类中LLM的增益边界
practical_value: '- 做检索增强的LLM分类/推荐任务时，优先用Distance-KNN作为baseline，尤其检索样本标签共识高的场景，KNN效果更优且推理成本仅为LLM的几十分之一

  - 低标签共识场景（如冷启动用户/商品分类、模糊query意图识别）可引入大参数LLM补充KNN不足，但需限定在检索样本与query距离较近的区间，远距场景LLM效果反而不如KNN

  - 处理结构化用户/商品特征的分类任务时，优先用特征空间检索而非文本嵌入检索，后者会带来15%以上的精度损失

  - 用小参数LLM做表格分类时，可测试自然语言序列化+规则增强的prompt格式，能带来3-5个百分点的精度提升'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
检索式ICL让冻结通用LLM无需微调即可完成表格分类任务，但过往研究无法区分性能增益来自检索样本选择还是LLM推理本身，也不清楚LLM相比直接对相同检索样本做距离加权投票的传统KNN方法有何增量价值，缺乏系统的受控对比来明确LLM在这类任务中的适用边界。
### 方法关键点
- 采用共享检索样本的对比协议：对每个测试样本，LLM和Distance-KNN使用完全相同的k=8个近邻样本，排除检索差异对结果的干扰
- 引入两个核心维度划分场景：标签共识（检索样本中多数类占比）、特征 proximity（测试样本与检索样本的平均距离百分位）
- 覆盖多变量鲁棒性测试：对比4款主流开源LLM（Qwen3-8B/32B、Gemma3-12B/27B）与Distance-KNN的表现，验证候选池大小、演示样本数、prompt格式、检索表示等变量的影响
### 关键结果
在19个公开表格分类数据集上的测试显示：
1. 所有候选池大小下，Distance-KNN平均精度均最高，全量候选池下精度达85.50%，仅比最强LLM Gemma3-27B的85.26%高0.24个百分点，但显著优于其他3款LLM
2. 低标签共识（≤4/8）场景下，Gemma3-27B相比KNN有3.6个百分点的精度增益，其中近邻/中邻区间增益最高达8.1个百分点，但远邻区间所有LLM均落后于KNN
3. 高标签共识（≥5/8）场景下，所有LLM均显著落后于KNN，最高落后幅度达9.91个百分点
### 核心结论
检索式表格分类任务中，绝大多数场景下距离加权KNN的性价比远高于通用LLM，仅在低标签共识且检索样本距离较近的细分场景下大参数LLM有增量价值
