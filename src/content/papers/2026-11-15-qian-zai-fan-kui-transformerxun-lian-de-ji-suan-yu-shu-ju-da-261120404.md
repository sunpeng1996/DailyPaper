---
title: Latent Feedback Is a Compute and Data Amplifier
title_zh: 潜在反馈：Transformer训练的计算与数据放大器
authors:
- Benhao Huang
- Chaitanya Dwivedi
- Xuezhe Ma
- Alexander Moreno
- Hector Liu
affiliations:
- Institute of Foundation Models
- USC
- CMU
arxiv_id: '2611.20404'
url: https://arxiv.org/abs/2611.20404
pdf_url: https://arxiv.org/pdf/2611.20404
published: '2026-11-15'
collected: '2026-11-17'
category: Training
direction: LLM训练优化 · 潜在反馈缩放定律
tags:
- Latent Feedback
- Scaling Law
- Transformer Training
- Compute Efficiency
- Data Efficiency
one_liner: 验证数据受限场景下潜在反馈比增加训练epoch更节省计算与独特数据
practical_value: '- 训练电商/推荐垂直域小LLM时，若高质量标注数据稀缺，可优先引入潜在反馈机制替代盲目堆epoch，同等效果下最多省48%训练计算、47%独特数据，且推理仅增加1个KV缓存向量，成本几乎无变化

  - 做LLM训练资源规划时，若模型单参数独特token数（UTPP）超过75（当前主流1B-10B模型UTPP普遍超过260），优先将计算资源投给潜在反馈而非增加训练epoch，收益更高

  - 推理成本敏感场景（如端侧推荐Agent、实时商品文案生成），不想提升模型参数量但要提效果时，可采用潜在反馈训练：训练仅增加20%-27% FLOPs，推理成本不变，效果等价于参数量放大1.14倍的普通Transformer'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM预训练瓶颈已从计算转向高质量稀缺数据，行业常用的多epoch重复训练收益边际递减，而潜在反馈机制此前未在相同计算开销下与多epoch训练做公平对比，实际落地价值未得到验证。
### 方法关键点
- 严格控制变量：对比基线为相同参数量、相同独特数据、相同计算预算的普通Transformer，唯一变量为训练策略
- 潜在反馈实现：每个token顶层隐状态经RMSNorm和投影矩阵后加入下一个token输入；训练时15%概率跑单遍，85%概率跑2遍（第一遍无梯度计算隐状态，第二遍计算损失回传），单token训练FLOPs仅比基线高20%~27%
- 拟合统一缩放定律，覆盖60M~778M参数量、12.5~400 UTPP（单参数独特token数）、1~4个epoch的全场景
### 关键结果
- 当UTPP>75时，潜在反馈在所有训练预算下都优于多epoch训练：UTPP=400、2个epoch时最多节省48%计算
- 相同epoch数下，潜在反馈最多节省47%独特数据：100 UTPP、3个epoch时271M模型可省41%数据
- 缩放定律在778M held-out集上损失预测误差仅0.3%，模型间效果差距预测误差仅0.05%
- 下游109个任务验证效果与验证集损失一致，UTPP>25时潜在反馈基本全面领先

当数据而非计算成为固定参数量模型训练的瓶颈时，把FLOP投给潜在反馈比投给更多训练epoch性价比高得多。
