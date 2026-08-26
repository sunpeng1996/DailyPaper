---
title: 'WeMM-Embedding: WeChat Multi-Modal Embedding Technical Report'
title_zh: 微信多模态通用嵌入模型WeMM-Embedding技术报告
authors:
- Junjie Zhou
- Ke Mei
- Lei Li
- Tianyi Wang
- Fengyun Rao
- Jing Lyu
affiliations:
- Tencent Inc. WeChat Vision
arxiv_id: '2608.24053'
url: https://arxiv.org/abs/2608.24053
pdf_url: https://arxiv.org/pdf/2608.24053
published: '2026-08-25'
collected: '2026-08-26'
category: GenRec
direction: 多模态嵌入 · 推荐搜索全链路落地
tags:
- Multimodal Embedding
- MLLM
- Semantic Retrieval
- RecSys
- Semantic ID
one_liner: 基于Qwen3.5的2B/4B/9B多模态嵌入模型，两阶段训练，开源多基准SOTA已在微信全场景落地
practical_value: '- 训练流程可复用：采用两阶段训练范式（大规模弱监督预对齐 + 小批量精标数据蒸馏），搭配Semantic ID引导的重采样解决语义分布偏置问题，适合电商图文/短视频商品的多模态召回、表征模型训练

  - 工程降本技巧：集成MRL嵌套表征学习，256维嵌入即可保留98.7%的2048维图像/视频任务性能，可直接降低向量检索的存储成本3/4、检索延迟至少50%，适配大流量在线场景

  - 全链路落地参考：多模态嵌入可直接复用在推荐全链路（召回、排序特征、用户序列建模、跨域内容匹配），微信实测14个A/B测试全涨点，对长尾内容、新发布内容的增益尤其明显

  - 低成本选型方案：开源2B版本性能超过主流8B开源多模态嵌入基线，中小团队可直接基于开源权重微调，替代传统CLIP风格表征，快速适配电商搜索、商品推荐、多模态RAG
  Agent等场景'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有CLIP风格多模态嵌入仅支持单模态/简单跨模态匹配，无法自然处理图文交错、视频带字幕等复合多模态输入；基于MLLM的通用嵌入方案存在小参数效率低、细粒度匹配效果差的问题，工业级场景亟需兼顾性能、部署成本、多场景适配的通用多模态表征方案。

### 方法关键点
- **模型架构**：基于Qwen3.5原生多模态基座，包含2B/4B/9B三个参数版本，追加专属<embedding>token取最后一层隐态做L2归一化输出；集成Matryoshka Representation Learning(MRL)，单次前向即可生成多维度嵌套嵌入。
- **数据构造**：统一pair式训练数据格式，覆盖弱监督跨模态对、caption对、检索对、分类对、QA对、分级relevance对6类数据；第二阶段精调数据集采用Semantic ID引导重采样解决语义分布偏置、MLLM过滤低质量对、针对性挖掘难负例。
- **训练策略**：两阶段训练，第一阶段用数亿级多模态数据做全局对齐，优化InfoNCE对比损失+分级相关性CoSENT损失+MRL多维度损失；第二阶段在精标数据上训练，叠加reranker细粒度排序监督、大模型跨尺寸嵌入蒸馏。

### 关键结果
MMEB-v2基准上，2B版本得分77.9超过SOTA 8B开源基线，9B版本得分80.6登顶公开榜单；12个跨模态检索基准平均得分81.7，性能超过Gemini Embedding 2等闭源商用模型；微信内部26任务基准平均得分72.0，14个线上A/B测试全链路涨点，已落地视频号、公众号、电商等全场景。

### 核心结论
小参数多模态嵌入模型通过高质量数据精调、分级监督、跨尺度蒸馏，可以达到甚至超过更大参数基线的效果，256维MRL嵌入即可保留98.7%的2048维图像/视频任务性能，兼顾效率与落地收益。
