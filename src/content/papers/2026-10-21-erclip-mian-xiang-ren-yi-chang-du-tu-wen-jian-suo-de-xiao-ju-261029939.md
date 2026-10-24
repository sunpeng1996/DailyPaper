---
title: 'ERCLIP: Small-Data Adaptation of CLIP for Free-Length Image-Text Retrieval'
title_zh: ERCLIP：面向任意长度图文检索的小数据CLIP适配方法
authors:
- Hoang-Bao Le
- Allie Tran
- Binh T. Nguyen
- Liting Zhou
- Cathal Gurrin
affiliations:
- ADAPT Centre, Dublin City University
- Ho Chi Minh University of Science, Vietnam National University
arxiv_id: '2610.29939'
url: https://arxiv.org/abs/2610.29939
pdf_url: https://arxiv.org/pdf/2610.29939
published: '2026-10-21'
collected: '2026-10-24'
category: Multimodal
direction: 多模态图文检索 · CLIP小数据适配
tags:
- CLIP
- Image-Text Retrieval
- Few-shot Learning
- Multimodal
- Long Text
one_liner: 仅用2%长标注数据微调CLIP，无推理开销提升长文本图文检索效果
practical_value: '- 电商商品图文匹配、多模态搜索场景可复用「训练侧长文本分句编码+融合、推理侧原生CLIP不变」的架构，无额外推理延迟，适配高QPS业务需求

  - 小样本微调预训练多模态模型时，可新增冻结原模型输出的preservation loss，降低微调对原有零样本能力的侵蚀，兼顾新场景效果和通用能力

  - 缺长文本标注的图文检索场景，仅需2万级配对数据即可获得接近百万级数据训练的长文检索效果，大幅降低标注成本'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
CLIP原生文本编码器仅支持77 token输入，长商品描述、详情文案等会被截断，现有长文图文检索方案依赖大量长标注数据，且会损害CLIP原有零样本能力，推理开销高。
### 方法关键点
1. 训练阶段将长caption拆分为符合77 token限制的句子，分别用CLIP编码后通过均值池化或门控残差Transformer融合，加对比损失对齐图文；
2. 推理阶段完全复用原生CLIP双编码器，无任何结构改动；
3. 新增冻结原CLIP的保留损失，约束图像和短文本embedding与原CLIP输出一致，降低零样本能力损耗。
### 关键结果
仅用2万对图文、1轮训练，长文本检索R@1较原生CLIP提升6.5~11.2个点，仅用LongCLIP 2%的标注数据就覆盖其62%~77%的效果提升；保留损失可恢复1.5~2.1个ImageNet零样本分类点，额外提升COCO图文检索R@1最高2.4个点，无额外推理成本。
