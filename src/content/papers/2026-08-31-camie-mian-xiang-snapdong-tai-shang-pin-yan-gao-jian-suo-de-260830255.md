---
title: 'CAMIE: Co-Engagement-Aware Multimodal Item Embeddings for Snap Dynamic Product
  Ads Retrieval'
title_zh: CAMIE：面向Snap动态商品广告检索的共交互感知多模态物品嵌入
authors:
- Xiaodong Liu
- Siman Wang
- Congfei Zhang
- Hsiang-wei Chao
- Xiao Bai
- Wen Zhang
- Jingxiao Ma
- Zhe Liu
- Yunzhi Zhou
- Yajun Wang
affiliations:
- Snap Inc.
arxiv_id: '2608.30255'
url: https://arxiv.org/abs/2608.30255
pdf_url: https://arxiv.org/pdf/2608.30255
published: '2026-08-31'
collected: '2026-09-01'
category: RecSys
direction: 多模态物品嵌入 · 广告I2I召回
tags:
- Multimodal Embedding
- I2I Retrieval
- Contrastive Learning
- MLLM
- Dynamic Product Ads
one_liner: 基于MLLM与共交互对比学习的统一多模态物品嵌入，大幅提升Snap DPA I2I检索性能
practical_value: '- 样本构造可直接复用：优先扩大共交互对规模（包含浏览、点击等低意图行为），比仅筛选高意图加购/下单对的收益更高，可直接应用在电商商品、内容、广告I2I嵌入的训练样本构建环节

  - 架构降本方案：用单个MLLM多模态嵌入checkpoint同时支撑多模态、纯文本I2I检索，性能仅比专属单模态模型低1~2pp，可大幅减少多套编码器、索引的运维成本

  - 迭代路径参考：共交互对比学习的监督信号贡献了80%+的效果提升，远高于MLLM本身的架构增益，资源有限的团队可先在现有CLIP类双塔模型上叠加共交互监督，再考虑升级MLLM架构

  - 场景选型参考：纯图像I2I检索场景仍建议使用SigLIP类双塔视觉编码器，MLLM在该场景下效果比双塔低18pp以上，无需为了统一架构强行上MLLM'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业级I2I召回是推荐广告系统的核心候选生成组件，现有方案存在两大痛点：一是模态碎片化，需维护文本、图像、多模态三套独立编码器、训练管线与ANN索引，运维成本高；二是纯内容监督的嵌入空间与用户实际交互行为对齐度差，无法匹配下游转化目标，亟需一套统一的多模态嵌入方案，同时对齐用户交互信号。
### 方法关键点
- 样本构造：从用户旅程中挖掘全漏斗共交互物品对，按7天半衰期赋权重，过滤跨广告主、跨一级类别的噪声对
- 模型架构：基于Qwen3-VL-Embedding 2B backbone，冻结主干加LoRA微调，统一处理多模态、纯文本、纯图像输入，共享投影头输出L2归一化嵌入
- 训练目标：采用对称批次内InfoNCE损失，跨设备聚合负样本，适配无向的物品共交互关系
- 部署方案：离线编码全量商品建ANN索引，在线按请求模态渲染输入后做ANN查询，延迟与传统I2I检索一致
### 关键结果
离线10M训练对、100K测试集上，Recall@10比最强商业多模态基线Gemini Embedding 2高6%；同个多模态checkpoint做纯文本检索仅比专属文本模型低1.1pp。线上A/B测试替换原有两套内容编码器，多模态场景CTR+0.390%、CVR+10.832%，纯文本场景CTR+18.958%、CVR+13.12%，整体DPA流量CTR+0.211%、CVR+1.911%。
### 核心结论
共交互监督信号的价值远大于模型架构本身，MLLM的核心价值是用一套 checkpoint 低成本覆盖多模态和纯文本检索场景，而非单纯的效果提升。
