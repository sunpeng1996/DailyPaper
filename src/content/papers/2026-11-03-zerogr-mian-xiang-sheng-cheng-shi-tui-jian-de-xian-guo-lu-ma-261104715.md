---
title: 'ZeroGR: Filtering-First Constrained Decoding for Generative Recommendation'
title_zh: 《ZeroGR：面向生成式推荐的先过滤约束解码系统》
authors:
- Xiangrui Yang
- Jiawei Yang
- Liang Zeng
- Daqian Ding
- Ziqian Liu
- Bing Tian
- Cheng Peng
- Yunfeng Zhao
- Fangyu Zhang
- Jiaqiang Liu
affiliations:
- The University of Hong Kong
- Peking University
- Kuaishou Technology
- Huazhong University of Science and Technology
arxiv_id: '2611.04715'
url: https://arxiv.org/abs/2611.04715
pdf_url: https://arxiv.org/pdf/2611.04715
published: '2026-11-03'
collected: '2026-11-04'
category: GenRec
direction: 生成式推荐 · 约束解码优化
tags:
- Generative Recommendation
- Constrained Decoding
- Semantic ID
- GPU Acceleration
- Serving System
one_liner: 提出面向生成式推荐的先过滤后约束解码系统，相比基线最高加速9.9倍，显存占用降74.5%
practical_value: '- 生成式推荐业务落地可直接替换原有先打分后过滤的约束解码流程，先过滤后打分的方案返回结果与原有流程重叠99.9%，对推荐效果影响可忽略，同时大幅降低无效计算

  - SID生成解码的索引优化可复用step-sliced设计，根据每步有效候选密度选择稀疏/稠密索引表示，相比全量Trie索引显存占用最高降74.5%，适合千万级以上商品的生成式推荐场景

  - GPU推理优化可复用shared-slot执行+hybrid projection策略，根据每步工作负载动态选择全量/选择性投影，既避免稀疏计算的GPU效率损失，又能最大化节省无效打分开销，加速比最高达9.9倍

  - 热更新场景可复用layout-guided流式索引构建方案，CPU并行构建索引片段+双缓冲异步传输到GPU，索引重建速度提升278倍，基本不影响线上服务可用性'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有基于Semantic ID的生成式推荐普遍采用先全量打分后过滤无效SID的约束解码流程，90%以上的计算浪费在后续会被丢弃的无效候选上；同时传统前缀树过滤索引显存占用高、更新慢，成为生成式推荐落地的核心性能瓶颈。行业此前普遍担心先过滤后打分的逻辑会改变概率归一化逻辑、影响推荐效果，因此该方案未被广泛采用。

### 方法关键点
- 验证先过滤后打分的可行性：实验证明两种解码流程返回结果重叠99.9%，Recall指标几乎一致，效果损失可忽略
- 设计step-sliced过滤索引：按解码步拆分索引，每步根据有效候选密度自动选择稠密/稀疏表示，大幅降低显存占用
- 执行引擎采用shared-slot+hybrid projection：所有解码阶段共享固定候选槽位降低数据交换开销，每步根据负载自动选择全量投影（适合稠密步）或选择性投影（适合稀疏步），最大化GPU执行效率
- 流式索引更新：预计算索引布局，CPU并行生成索引片段后双缓冲异步上传GPU，减少对线上服务的干扰

### 关键实验
在快手工业级搜索、短视频推荐数据集上对比Unconstrained、STATIC、FlashTrie、CPU Trie四类基线，解码链路最高加速9.9倍，GPU索引显存占用降低74.5%，索引重建速度提升278倍。

> 最值得记住：生成式推荐约束解码中，先过滤后打分的优化几乎不影响推荐效果，却能带来数量级的性能提升，是生成式推荐落地的核心工程优化方向
