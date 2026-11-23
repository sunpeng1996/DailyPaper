---
title: 'Run One, Get Two: Near-Free Streaming Safety Checks for Local LLMs'
title_zh: 《一次运行双重收益：本地LLM接近零开销的流式安全检测》
authors:
- Soheil Zibakhsh
- Pedram Aghazadeh
- Farinaz Koushanfar
affiliations:
- University of California San Diego
arxiv_id: '2611.26975'
url: https://arxiv.org/abs/2611.26975
pdf_url: https://arxiv.org/pdf/2611.26975
published: '2026-11-20'
collected: '2026-11-23'
category: LLM
direction: LLM推理优化 · 流式安全检测
tags:
- LLM Safety
- LoRA
- KV Cache
- Triton Kernel
- Streaming Moderation
one_liner: 通过共享生成器权重、KV缓存和双行Triton内核，实现接近探针成本的专用guard级流式安全检测
practical_value: '- 对于在端侧/本地部署LLM导购、对话Agent的电商业务，可复用ToRA的共享权重+KV缓存架构，几乎不增加推理延迟即可接入安全检测，避免额外部署guard模型的成本与延迟开销

  - 可复用双行Triton内核的设计思路，将低优先级token级辅助任务（如生成内容合规检测、商品推荐相关性判断）与主生成任务融合执行，充分利用单batch内存-bound解码场景下的闲置算力

  - 做流式任务监督时，可借鉴中间token采样打标的方法，在仅增加少量标注成本的前提下，大幅提升流式场景下的风险检测响应速度，无需等待完整序列生成再判定'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
本地单用户部署的LLM（如端侧导购Agent、私域生成式服务）解码为内存带宽 bound，大量算力闲置；现有流式安全检测方案存在严重的精度-效率 tradeoff：专用guard模型精度高但会让单token延迟提升80%+，隐状态探针成本低但精度差，且等完整回复生成再拦截无法避免有害内容触达用户，亟需低开销高准确的流式检测方案。

### 方法关键点
- 架构：仅在生成器上层K层Transformer的FFN插入LoRA适配器，分支为安全检测分支，分支前的计算、注意力权重、KV缓存完全复用生成器结果，无需额外维护KV缓存，不影响生成器输出。
- 训练：冻结生成器权重，仅训练LoRA参数和分类头；除序列最终标签外，对响应中间token采样打标，不安全内容从首次出现的onset位置开始标注正例，提升流式检测响应速度。
- 工程：自研双行Triton内核，一次读取权重同时计算生成与检测分支结果，仅对检测分支应用LoRA更新，保证生成器输出与原模型比特级一致，无精度偏差。

### 关键实验结果
在Qwen3-0.6B上测试17个安全基准：ToRA平均响应F1比专用Qwen3Guard-Stream高1.0，平均prompt F1高1.7，12个基准超过后者；比隐状态探针SingProbe响应F1高3.8，同误报率下不安全响应检出率高11.8个百分点。2k上下文下仅增加3.5%的单token延迟，远低于专用guard的85.9%，额外内存占用仅9.3MiB，无额外KV缓存开销。

### 核心洞察
单batch内存-bound的LLM解码场景下，通过共享计算资源与融合内核，可几乎零成本接入token级辅助任务，无需牺牲主任务的性能与精度。
