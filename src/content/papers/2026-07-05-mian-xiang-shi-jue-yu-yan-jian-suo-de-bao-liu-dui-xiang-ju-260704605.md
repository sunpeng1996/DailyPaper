---
title: Do All Visual Tokens Matter Equally? Object-Evidence Preserving Token Merging
  for Vision-Language Retrieval
title_zh: 面向视觉语言检索的保留对象证据的Token合并方法
authors:
- Suhyeong Park
- Junha Jung
- Jungwoo Park
- Jaewoo Kang
affiliations:
- The Catholic University of Korea
- Korea University
- AIGEN Sciences Inc.
arxiv_id: '2607.04605'
url: https://arxiv.org/abs/2607.04605
pdf_url: https://arxiv.org/pdf/2607.04605
published: '2026-07-05'
collected: '2026-07-07'
category: Multimodal
direction: 多模态检索 · 视觉Token高效压缩
tags:
- Vision-Language Retrieval
- Token Merging
- Multi-vector Retrieval
- Efficient Inference
- Late Interaction
one_liner: 提出训练用对象标注先验、推理无检测器的SaMer框架，压缩视觉Token同时提升多向量检索精度
practical_value: '- 多模态商品检索场景可直接复用SaMer框架压缩图像侧Token，在降低存储与计算成本的同时保留细粒度商品特征匹配能力，提升图文检索准确率

  - 训练时用弱监督/标注的对象信息作为Token合并先验、推理无需检测器的设计，可低成本落地到已有的多模态检索链路，无需改动现有视觉、语言 backbone

  - 保留对象级证据的压缩思路可迁移到生成式推荐的多模态Item表征压缩，降低RAG检索阶段的存储开销与匹配延迟'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
多向量视觉语言检索依赖最大相似度晚交互保留细粒度视觉证据，但图像侧稠密Token带来极高的存储与打分成本；现有Token压缩方法易丢失/坍缩查询所需的对象、区域级证据，导致检索精度下降。
### 方法关键点
提出SaMer对象感知Token合并框架：1）训练时仅用对象标注作为合并先验，避免跨实例特征混合，推理无需真实边界框或检测器；2）仅微调共享投影层，冻结视觉与语言 backbone；3）压缩后仍保留原晚交互接口，无需修改下游检索逻辑。
### 关键结果
K=64时可移除93%以上的图像侧Token，将ColPali存储开销降低16.09×，同时提升Flickr30K、MSCOCO数据集的R@1指标，优于现有压缩基线，短语级grounding能力也更优。
