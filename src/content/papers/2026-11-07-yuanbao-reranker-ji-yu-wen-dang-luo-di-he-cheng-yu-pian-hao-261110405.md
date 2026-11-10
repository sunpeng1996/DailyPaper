---
title: 'Yuanbao-Reranker: Document-Grounded Synthesis and Preference Distillation
  for Text Reranking'
title_zh: Yuanbao-Reranker：基于文档落地合成与偏好蒸馏的文本重排模型
authors:
- Hongyuan Xu
- Dezhi Ye
- Jiahao Cao
- Jie Liu
- Haijin Liang
- Haibo Shi
- Jin Ma
affiliations:
- Yuanbao Search, Tencent Inc.
arxiv_id: '2611.10405'
url: https://arxiv.org/abs/2611.10405
pdf_url: https://arxiv.org/pdf/2611.10405
published: '2026-11-07'
collected: '2026-11-10'
category: RecSys
direction: 文本重排·搜索推荐RAG通用优化
tags:
- Reranker
- Preference Distillation
- Synthetic Data
- Hard Negative Mining
- Model Merging
one_liner: 推出覆盖0.6B/4B/8B参数规模的通用文本重排器，跨多领域多语言显著优于同规模基线
practical_value: '- 数据构造可直接复用：做电商/搜索推荐重排时，可采用答案优先的文档落地query合成+按领域/文本长度配额采样的方式，扩充训练数据同时避免短文本/热门领域偏置

  - 负例采样trick：负例挖掘时用教师模型设置分数阈值过滤假负，再按难度分层采样Hard/Medium/Moderate三类负例，能大幅提升细粒度排序效果

  - 训练目标优化：重排训练可采用点wise交叉熵+有界最小间隔hinge损失的组合，同时加入负例之间的顺序约束，避免MSE回归的过约束问题，提升负例排序精度

  - 模型合并技巧：训练多组不同配置的重排模型后，用层wise自适应LERP合并，无需额外推理成本就能带来0.5-1个点的效果提升，适合线上部署'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有文本重排器训练存在三大痛点：公开标注数据领域和query类型覆盖窄，无约束合成query易遗漏约束、泄露答案；样本筛选易偏向短百科文本，长文档/专业领域样本严重不足；仅用二分类标签训练忽略负例间的相对相关性，直接回归教师分数差易过约束已区分的样本，难以兼顾不同参数量级模型的精度和部署 latency 要求。
### 方法关键点
- 数据构造：采用答案优先+query类型引导的文档落地合成，生成query时保留完整约束且不泄露答案，再经教师验证、语义去重、按领域/长度配额分配的三级筛选流程，保证样本质量和覆盖均衡
- 负例构造：对每个正例从真实检索池召回候选，用教师模型分数差>1过滤假负，再分层采样Hard/Medium/Moderate三类负例，生成2.75M 1:3的排序组
- 训练优化：联合优化点wise二分类交叉熵和有界最小间隔hinge损失，同时约束正-负和负-负对的顺序，间隔上限设为4避免过约束，支持跨规模和同规模蒸馏，最后用层自适应LERP合并多组模型
### 关键实验
在中文CMTEB-R、多语言MMTEB-R、英文BEIR、长文档MLDR、代码MTEB-Code五大基准测试：0.6B版本平均得分70.96，超同规模基线3.64点，优于1B-4B基线；4B版本平均得分73.63，超8B教师模型0.95点；8B版本平均得分74.21，达到SOTA，且效果不依赖第一阶段召回器，跨召回器仍保持2-4个点提升。
### 核心结论
重排训练的效果提升核心来自高质量样本构造、分层难负例采样，以及兼顾点wise分类和相对排序的软约束损失，而非单纯扩大模型规模。
