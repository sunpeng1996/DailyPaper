---
title: 'Tandem: Serving Hybrid Linear-Attention GUI Agents on Mobile NPUs'
title_zh: Tandem：移动端NPU上混合线性注意力GUI Agent运行时系统
authors:
- Zhuomin Chen
- Jingchao Ni
- Xu Zheng
- Yong Chen
- Mo Sha
- Wei Cheng
- Dongsheng Luo
affiliations:
- Florida International University
- University of Houston
- NEC Laboratories America
- Singapore Management University
arxiv_id: '2610.26660'
url: https://arxiv.org/abs/2610.26660
pdf_url: https://arxiv.org/pdf/2610.26660
published: '2026-10-19'
collected: '2026-10-21'
category: Agent
direction: 移动端GUI Agent NPU推理优化
tags:
- MobileAgent
- NPU
- LinearAttention
- InferenceOptimization
- SpeculativeDecoding
- GUI
one_liner: 面向移动端GUI Agent场景，设计NPU推理运行时，较基准降30%时延、33%能耗
practical_value: '- 端侧电商/交互Agent部署可复用分歧点checkpoint策略：无需按chat场景消息边界存checkpoint，直接在连续请求的最长公共前缀分歧点存状态，可减少上百个token的重复prefill开销，直接降端侧推理时延

  - 短输出端侧Agent（如返回操作指令、短推荐文案）的speculative decoding优化：仅保留末尾最多4个token的per-token回滚状态，前面所有输入走NPU矩阵单元prefill，既保留投机解码收益，又避免全段per-token执行的额外开销

  - 端侧模型驻留功耗优化技巧：请求间隙无需卸载模型，仅释放NPU算力投票即可，骁龙8 Elite上可将模型加载时的待机功耗从0.76W降至0.22W，同时避免9s模型冷启动开销

  - 混合线性注意力模型端侧部署性能优化：可直接复用SwiGLU算子融合、卷积通道优先内存布局的trick，减少中间内存流量，进一步提升推理效率'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
移动端GUI Agent执行任务时每步需读取屏幕后调用大模型输出操作指令，端侧NPU部署可避免隐私泄露、省去网络往返开销，但现有方案适配性差：混合线性注意力模型的chat场景checkpoint策略无法匹配Agent请求前缀常在中间分歧的特性，导致大量token重复计算；投机解码的rollback状态生成会将prefill从NPU矩阵单元移到per-token执行，短输出场景下额外开销远大于解码收益；模型驻留时NPU持续保持唤醒，待机功耗过高。
### 方法关键点
- 分歧点checkpoint：对比连续请求的最长公共前缀，满足≥32token间隔阈值时在分歧点保存recurrent state，大幅减少重复prefill
- 回滚感知prefill：前n-K个token走NPU矩阵单元批量prefill，仅末尾K个token（K为最大草稿数+1）走per-token路径生成rollback state，兼顾投机解码需求与prefill效率
- 解码优化：设计列共享验证核实现多草稿权重读取共享，裁剪MTP草稿头的输出词表到高频32768个token，降低解码开销
- 空闲功耗释放：3s无请求时释放NPU算力投票，保留模型权重在内存，避免冷启动同时降低待机功耗
### 关键结果
在骁龙8 Elite上对比llama.cpp最快NPU配置：文本场景每步时延降30%、能耗降33%，截图场景时延降16%，模型加载时的待机功耗从0.76W降至0.22W；下一代骁龙平台上文本时延仍降27%，优化效果跨代通用。
> 最值得记住：端侧Agent推理优化要紧贴场景特性（短输出、前缀重复、闲时多），不要直接照搬云端chat场景通用策略
