---
title: Why Is Video Still So Expensive? A Survey of Inference-Efficiency Mechanisms
  in Video and Audiovisual LLMs
title_zh: 视频与音视频大语言模型推理效率机制综述
authors:
- Killian Steunou
- Yannis Tevissen
- Mounîm A. El Yacoubi
affiliations:
- Institut Polytechnique de Paris
- Télécom SudParis
- Moments Lab
arxiv_id: '2609.10355'
url: https://arxiv.org/abs/2609.10355
pdf_url: https://arxiv.org/pdf/2609.10355
published: '2026-09-09'
collected: '2026-09-10'
category: Multimodal
direction: 多模态大模型 · VideoLLM推理效率优化
tags:
- VideoLLM
- Inference Efficiency
- Multimodal LLM
- Token Pruning
- KV Cache
one_liner: 系统梳理VideoLLM全流水线优化机制，汇总同宿主下性能成本对比，明确评估缺口
practical_value: '- 做商品视频导购、短视频内容理解的业务可优先做全流水线分层优化：前端先落地query感知的轻量帧采样（如TSPO仅3.5M参数，比均匀采样精度高5点），投入产出比远高于后端LLM单点优化。

  - 针对直播QA、长视频商品检索等KV缓存压力大的场景，可复用token剪枝+KV压缩组合策略，现有方案能在保留98%精度下将LLM预填充速度提升6倍以上。

  - 端侧短视频内容推荐场景可直接选型轻量化视频编码器（如MobileViCLIP比大编码器快55倍，检索精度持平），大幅降低端侧推理成本。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
VideoLLM在视频caption、QA、检索等任务效果显著，但推理成本随帧数、上下文长度线性增长，无法落地实时、移动端、资源受限场景；现有优化方法分散在不同pipeline阶段，缺乏统一的性能-成本对比框架，音视频联合优化评估标准不统一，难以指导业务选型。

### 方法关键点
- 按VideoLLM标准4阶段流水线（输入构建→编码器→连接器→LLM执行）分类所有效率优化机制，覆盖2022年至今的125篇相关工作，包含仍在使用的早期帧采样、视觉编码器方案。
- 严格区分同宿主、同输入协议下的可比实验结果，避免跨论文异质性对比偏差，单独梳理音视频联合优化路径（音频剪枝、音频引导视觉采样等）。
- 开源了相关方法汇总仓库：https://github.com/momentslab/awesome-efficient-videollm。

### 关键结果
- 帧采样层：同LLaVA-Video-7B、64帧预算下，query感知的TSPO采样器仅增加3.5M参数，LongVideoBench精度比均匀采样高5个点，32帧选择方案即可达到64帧均匀采样的精度。
- 编码器层：Hiera、UniFormerV2等池化注意力架构比同精度的卷积/状态空间编码器快2倍以上，MobileViCLIP在移动端比InternVideo2-L14快55.4倍，零样本检索精度持平。
- 连接器/LLM层：FlashVID等token剪枝方案在保留99.1%精度下，LLM预填充速度提升6.3倍，KV压缩方案可降低70%以上的生成latency。

最值得记住的结论：VideoLLM效率优化的核心是全流水线逐层平衡时空信息保留度与计算/内存开销，上游帧采样、编码器优化的投入产出比通常远高于下游LLM侧单点优化。
