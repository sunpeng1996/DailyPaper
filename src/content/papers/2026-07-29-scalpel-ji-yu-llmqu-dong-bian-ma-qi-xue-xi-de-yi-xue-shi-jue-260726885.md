---
title: 'SCALPEL: Semantic Cross-modal Alignment via LLM-Powered Encoder Learning for
  Medical Vision-Language Representation'
title_zh: SCALPEL：基于LLM驱动编码器学习的医学视觉语言跨模态对齐框架
authors:
- Yunzhan Fu
- Enyu Bao
- Xiangyu Shen
- Yihao Wu
- Chunbo Jiang
- Fangli Guan
- Liqi Yan
affiliations:
- School of Computer Science, Hangzhou Dianzi University, China
arxiv_id: '2607.26885'
url: https://arxiv.org/abs/2607.26885
pdf_url: https://arxiv.org/pdf/2607.26885
published: '2026-07-29'
collected: '2026-07-31'
category: Multimodal
direction: 医学多模态 · LLM驱动跨模态对齐
tags:
- Vision-Language Pre-training
- Contrastive Learning
- Cross-modal Alignment
- LLM Encoder
- Multimodal Representation
one_liner: 针对医学VLP融合LLM的三类瓶颈提出优化框架，在多类医疗多模态任务上取得SOTA
practical_value: '- 可迁移「生成式LLM转各向同性编码器」的对比微调方案，解决电商场景长文本（商品详情、用户评论）的表示坍塌问题

  - 不对称对齐+离线特征缓存的训练策略可直接复用在大batch多模态召回训练场景，大幅降低显存开销

  - 细粒度属性感知的对比损失设计思路，可用于电商多模态匹配中规避颜色/尺寸/规格等属性混淆的匹配错误'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有医学VLP框架的轻量文本编码器处理长、术语密集的临床报告时，受限于上下文窗口小、表征能力弱；融合医疗LLM又存在三类瓶颈：生成式LLM在标准对比目标下各向异性表征坍塌、大batch端到端联合训练显存开销过高、普通对比损失忽略细粒度属性导致幻觉。
### 方法关键点
1. 临床报告对比微调：将生成式LLM通过领域文本适配为各向同性编码器
2. 非对称对齐策略：用离线特征缓存降低训练显存开销
3. 解剖-否定感知目标：显式惩罚侧性混淆、错误否定的图文不匹配对
### 关键结果
在MIMIC-CXR、CheXpert、IU X-Ray基准上，跨模态检索、零样本疾病分类、医疗VQA三类任务均达到SOTA性能
