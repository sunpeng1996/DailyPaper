---
title: 'Chaos in the Text: Revealing the Modality Preference in Mixed-Modality Retrievers'
title_zh: 揭示混合模态检索器的模态偏好问题及Trident优化框架
authors:
- Yubo Sun
- Chunyi Peng
- Yukun Yan
- Zhenghao Liu
- Zhipeng Xu
- Sen Mei
- Linlin Xin
- Zheni Zeng
- Maosong Sun
affiliations:
- University of the Chinese Academy of Sciences
- Northeastern University
- Tsinghua University
- Nanjing University
arxiv_id: '2610.11816'
url: https://arxiv.org/abs/2610.11816
pdf_url: https://arxiv.org/pdf/2610.11816
published: '2026-10-07'
collected: '2026-10-09'
category: RAG
direction: 多模态检索 · 跨模态偏好校准
tags:
- Multimodal Retrieval
- Modality Bias
- Contrastive Learning
- InfoNCE
- RAG
one_liner: 发现混合模态检索器普遍存在文本偏好偏差，提出Trident框架实现跨模态分数可比与稳定检索
practical_value: '- 电商多模态商品搜索/召回场景可复用Trident多视图正例构造逻辑，将同一款商品的文本详情、主图、图文混排详情作为对等正样本训练，避免无关文本挤掉相关商品图的排序

  - 多模态RAG问答Agent可借鉴Multi-Positive View InfoNCE损失优化检索模块，无需额外后处理校准即可降低文本干扰对图文混排知识库检索效果的影响

  - 业务上若存在图文混合候选池排序场景，可先验证现有模型模态偏好：加入等量无关文本/图像干扰项，若NDCG下降差超过0.3，可引入Trident做低成本微调'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多模态检索器在单模态语料上性能优异，但真实业务场景（电商商品库、企业知识库等）普遍存在文本、图像、图文融合三类文档混合的情况，实测发现这类检索器在混合语料上性能呈V型下降，无关文本对排序的干扰远高于等量无关图像，甚至会把相关图像挤出Top-K，该“文本混乱”现象核心是模型存在系统性文本偏好，跨模态相似度分数不可比，亟需从训练层面解决。

### 方法关键点
- 多模态正视图构造：对每个文档生成三个语义对等的视图——文本视图（图像转文本描述）、图像视图（原图）、融合视图（图像+短摘要），三者作为同一查询的对等正样本
- Multi-Positive View InfoNCE损失：将三个正样本与批次内负样本放入同一softmax空间做归一化，损失拆分为「相关性判别（正样本整体得分高于负样本）」和「正视图平衡（避免概率质量集中在单一模态）」两部分，强制跨模态分数可比

### 关键实验
在ChartQA、SlideVQA等6个视觉文档检索基准上测试，对比CLIP系、VLM系10+基线，Trident优化后的Qwen3-VL-2B在混合模态语料上平均NDCG@10达73.9，比原生8B版本高出26.73，同时单模态语料平均性能提升2.92，对语料模态比例变化的敏感度降低80%以上，无关文本干扰导致的性能下降幅度减少70%。

### 核心结论
多模态检索的效果不能只看单模态基准，混合模态下的模态偏好才是真实业务落地的核心瓶颈，通过多正视图联合对比学习可以从根源上解决跨模态分数不可比问题。
