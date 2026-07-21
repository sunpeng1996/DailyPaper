---
title: 'WHALE: A Scalable Unified Model for Recommendation with Wukong-HSTU Architecture'
title_zh: WHALE：基于Wukong-HSTU架构的可扩展统一推荐模型
authors:
- Renqin Cai
- Dawei Sun
- Yuanjun Yao
- Zhiyong Wang
- Velvin Fu
- Maggie Zhuang
- Yu Shi
- Zhongnan Fang
- Xuan Cao
- Jing Qian
affiliations:
- Meta Platforms, Inc.
arxiv_id: '2607.17017'
url: https://arxiv.org/abs/2607.17017
pdf_url: https://arxiv.org/pdf/2607.17017
published: '2026-07-19'
collected: '2026-07-21'
category: RecSys
direction: 推荐排序 · 特征与序列统一建模
tags:
- Ranking
- Feature Interaction
- Sequential Recommendation
- Scalable RecSys
- Industrial Deployment
one_liner: 融合Wukong特征交互与HSTU长序列建模的层间注意力可扩展工业推荐架构
practical_value: '- 架构迭代：现有系统若已独立部署特征交互、长序列建模模块，无需推翻重构，可直接采用层内交叉注意力融合方案，让高阶特征交叉按需调取细粒度行为证据，避免浅融合（序列压缩后输入特征模块）的信息损失

  - 工程提效trick：跨分支注意力可直接复用KV共享的Triton定制核，SwiGLU采用共享门权重设计，训练推理吞吐量提升30%左右，无明显精度损失

  - 部署优化：动态形状推理场景引入shape hint消除CPU-GPU同步点，配合AOT算子融合，可提升22%左右推理QPS，适配高流量排序场景的latency约束

  - 扩容优先级：单位算力收益从高到低为长序列扩容（3k→15k）> 模型宽度增加（64→512维）> 层深增加（2→8层），资源有限时可优先拉长用户行为序列长度'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业推荐的两大核心建模方向（非序列特征高阶交互、长用户行为序列建模）长期走独立演进路线，主流浅融合方案仅将序列压缩为固定向量后输入特征交互模块，导致高阶特征交叉无法按需调取细粒度行为证据，无法发挥两类架构的互补优势，同时现有融合方案难以满足工业级部署的吞吐、延迟约束。

### 方法关键点
- 每层WHALE包含3个核心模块：Wukong模块建模用户/物品/上下文的非序列特征高阶交互，HSTU模块建模长行为序列的时序依赖，注意力融合模块用Wukong输出作为Query、HSTU输出作为KV做交叉注意力，逐层实现两个分支的信息交换
- 训练优化：定制Triton跨分支注意力核，KV共享减少显存带宽占用；SwiGLU采用共享门权重，减少33%FFN矩阵乘法；混合精度训练+torch.compile提升训练吞吐
- 推理优化：AOT编译算子融合，shape hint消除CPU-GPU同步，适配动态形状场景降低延迟

### 关键实验
基于Meta短视频平台80B训练样本、4B测试样本，对比Wukong-only、HSTU-only基线：相同算力下WHALE较Wukong基线最高获1.39% NE gain，较HSTU基线最高获0.56% NE gain；序列长度从3k升至15k带来0.95% NE gain，层深从2升至8带来0.28% NE gain，维度从64升至512带来0.4% NE gain；在线A/B测试核心业务指标提升0.113%，两类辅助 engagement 指标分别提升0.824%、1.82%，仅损失5%推理QPS，满足上线要求。

**最值得记住的一句话**：工业推荐的下一轮scaling收益不只来自单个backbone的容量放大，更来自互补架构在每一层的渐进式统一融合。
