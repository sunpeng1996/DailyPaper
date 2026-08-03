---
title: 'Faster but Different: Diagnosing and Controlling Content Drift in Accelerated
  Multimodal Diffusion Language Models'
title_zh: 加速多模态扩散大模型的内容漂移诊断与控制方法
authors:
- Yaoxuan Dou
- Yang Shu
affiliations:
- Beijing Institute of Technology
- Zhejiang University
arxiv_id: '2607.29079'
url: https://arxiv.org/abs/2607.29079
pdf_url: https://arxiv.org/pdf/2607.29079
published: '2026-07-31'
collected: '2026-08-03'
category: LLM
direction: 多模态LLM · 推理加速一致性优化
tags:
- dMLLM
- KV cache
- inference acceleration
- content drift
- diffusion LLM
one_liner: 发现加速多模态扩散大模型内容漂移源于KV缓存过期，调整刷新间隔可实现速度-一致性最优权衡
practical_value: '- 部署多模态Agent处理商品图、广告素材解析时，不要用置信度阈值控制输出一致性，优先调整KV cache刷新间隔，避免生成内容漂移导致下游推荐/搜索决策出错

  - 对输出稳定性要求高的场景（比如商品属性自动提取、合规文案生成），可将KV cache刷新间隔设为1，在保留1.3倍推理加速的同时实现与未加速模型几乎完全一致的输出

  - 上线任何LLM加速方案前，仅需数百次生成测试，用未加速输出做参考对比，即可快速排查加速带来的内容漂移问题，无需全量factuality评估'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
多模态Agent、商品素材解析、广告内容理解等低延迟业务场景广泛使用免微调的扩散大模型（dMLLM）加速方案，但加速过程会无感知改变生成内容，相同输入会得到不一致的中间结果，进而影响下游搜索、推荐、智能体决策的可靠性。而现有加速方案默认置信度阈值是速度-质量的调节旋钮，这一假设从未在多模态开放生成场景被验证。
### 方法关键点
- 以LLaDA-V 8B多模态扩散大模型为测试对象，对比Fast-dLLM加速输出与未加速基线的内容一致性，测试集包含300张MME基准的真实图像，覆盖艺术作品、OCR、场景等11类内容
- 先后扫描写信度阈值、KV cache刷新间隔两个核心参数，同时测试dLLM-Cache、LaViDa两个独立实现的一致性表现，验证结论通用性
- 额外测试7种自适应/平滑刷新策略，对比固定间隔刷新的性能表现
### 关键结果
- 置信度阈值在1.05~1.25 tokens/步的常用区间内对内容一致性无影响，加速后与基线的Jaccard相似度稳定在0.42左右，出现「开关效应」：开启加速后内容直接漂移，阈值无法调节
- 调整KV cache刷新间隔可实现单调的速度-一致性权衡：间隔设为1时可达到1.3倍加速，与未加速基线的Jaccard相似度达0.987，80%生成内容完全一致
- 所有测试的自适应刷新策略均无法在相同算力下超过固定间隔刷新的表现；dLLM-Cache需同时收紧两类缓存刷新间隔才能恢复一致性，会完全丧失加速优势

> 最值得记住的一句话：扩散大模型加速的内容一致性由KV cache刷新间隔决定，而非行业默认的置信度阈值。
