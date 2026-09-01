---
title: 'SnapBench: Benchmarking Snap-and-Ask Multimodal Retrieval for Mobile Interactions'
title_zh: SnapBench：移动端拍照提问场景多模态检索鲁棒性基准
authors:
- Zirong Chen
- Fuda Ye
- Kuan Zhang
- Enjun Du
- Junfu Pu
- Xinlei Wang
- Xinyu Zuo
- Lisheng Duan
- Jin Ma
- Yongqi Zhang
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- Tencent Yuanbao
- Tsinghua University
- ARC Lab, Tencent
- The University of Hong Kong
arxiv_id: '2608.29607'
url: https://arxiv.org/abs/2608.29607
pdf_url: https://arxiv.org/pdf/2608.29607
published: '2026-08-30'
collected: '2026-09-01'
category: Eval
direction: 多模态检索 · 鲁棒性评测基准
tags:
- Multimodal Retrieval
- Benchmark
- Robustness
- Modality Fusion
- Mobile AI
one_liner: 推出首个配对式移动端拍问多模态检索鲁棒性基准，配套无训练自适应融合方案MOOR
practical_value: '- 电商拍图搜、多模态商品检索场景可直接复用论文提到的53种图像/文本扰动算子，离线评测模型鲁棒性，提前识别低光照、模糊、打字错误等边缘case的性能衰减

  - 多模态检索的融合层可直接落地MOOR方案：无需训练、无需修改模型结构，仅基于各模态检索得分的分布一致性和方差动态加权，可解决粗粒度用户提问导致的"coarse-text
  drag"问题，实测提升明显

  - 多模态检索的鲁棒性测试不能仅做单模态扰动，需额外增加双模态同时扰动的测试用例，避免实际业务中双噪声场景下的性能超预期下跌

  - 构建业务检索评测集时可复用"固定gallery+仅扰动query"的配对设计，能精准量化各类输入问题对检索效果的影响，排除候选集变动的干扰'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
移动端拍图提问是移动AI高频入口，真实场景中拍摄的图像常存在模糊、裁剪、低光照等问题，用户文本提问多短、泛化甚至存在输入错误，现有基准要么仅测试干净输入，要么扰动时未固定检索目标、候选集与标注，无法精准量化噪声对检索效果的影响，也未覆盖双模态同时受损的真实场景。

### 方法关键点
- 构建SnapBench配对式评测基准：包含1145条查询、9085个gallery item，覆盖53种可控扰动（45种图像扰动、8种文本扰动），所有扰动仅修改query，检索目标、候选集、标注完全固定，可精准隔离噪声的影响
- 提出无训练自适应融合方案MOOR：基于各模态检索得分与图像-only检索路径的相关性、得分方差，动态加权4条模态匹配路径，无需修改模型结构、无需额外训练

### 关键结果
- 测试16个主流多模态检索模型（含双塔编码器、VLM embedding类），高严重度图像扰动最高可导致R@1下降16.3个点，文本扰动对联合检索的影响小于1个点
- 双模态同时扰动的R@1下跌幅度比单模态下跌之和平均高7.6个点，呈超加性，无法通过单模态鲁棒性测试结果预测
- MOOR相比固定融合策略，在干净/文本扰动/图像扰动场景下，双塔模型平均R@1提升10~18个点，VLM embedding类模型平均提升8~10个点

最值得记住的结论：固定权重的多模态融合无法适配不同查询的模态信号可靠性差异，是当前拍问类多模态检索效果劣化的核心瓶颈。
