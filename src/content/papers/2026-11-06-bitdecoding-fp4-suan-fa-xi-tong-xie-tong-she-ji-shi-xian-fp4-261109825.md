---
title: 'BitDecoding-FP4: Native FP4 KV Cache Decoding via Algorithm-System Co-Design'
title_zh: BitDecoding-FP4：算法系统协同设计实现原生FP4 KV缓存解码
authors:
- Dayou Du
- Woon Yee Ng
- Guangming Sheng
- Nick Lau
- Jianyi Cheng
- Luo Mai
affiliations:
- University of Edinburgh
- Tencent Hunyuan
arxiv_id: '2611.09825'
url: https://arxiv.org/abs/2611.09825
pdf_url: https://arxiv.org/pdf/2611.09825
published: '2026-11-06'
collected: '2026-11-09'
category: LLM
direction: LLM推理优化 · KV缓存量化
tags:
- KV cache
- FP4 quantization
- LLM serving
- system co-design
- Tensor Core
one_liner: 通过算法系统协同设计，在精度损失低于0.5个点的前提下实现FP4 KV缓存2.4~3.0倍的LLM服务吞吐提升
practical_value: '- 长上下文Agent、生成式推荐服务可直接复用该方案，在几乎无精度损失的前提下将KV缓存容量压缩3.5倍，支撑更高并发、更长用户行为序列的在线推理

  - 低比特量化优化可复用三类误差抑制trick：双残差Query量化降logit误差、下溢感知缩放解决长上下文概率归零、离群值感知Key量化抑制通道离群点

  - 工程端可复用转置Softmax融合量化、堆叠Query MMA的核优化思路，在Blackwell架构GPU上可实现接近3倍的解码kernel加速，无需改动上层业务逻辑'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
长上下文LLM服务中KV缓存占内存和带宽开销的主导地位，现有FP4 KV方案存在明显短板：直接量化的方案精度损失可达8.5个点，而精度导向的4-bit量化方案依赖向量码本，查表开销会严重降低解码吞吐，算法量化和系统加速之间存在核心gap。
### 方法关键点
- 算法层针对三类量化误差精准优化：
  1. 双残差Query量化：将Query拆为两个FP4张量累加，把Query带来的logit误差从60%降至1%
  2. 下溢感知概率缩放：通过指数重缩放和自适应scale选择，避免长上下文下小概率值被E4M3格式归零
  3. 离群值感知Key量化：结合静态平滑、Hadamard旋转、尺度搜索，抑制token级量化下的Key通道离群点误差
- 系统层核优化适配硬件特性：
  1. 转置Softmax融合概率量化，并行化Softmax reduction消除计算瓶颈
  2. 堆叠Query MMA将两个残差Query合并到一次Tensor Core运算，额外开销控制在4%以内
  3. 适配分页KV缓存，采用混合精度存储（BF16存最近token和attention sink，FP4存历史页）降低元数据开销
### 关键结果
在Qwen3-4B/30B、GLM-4.7（355B）、Hy4-preview（770B）等稠密/MoE模型上测试，对比BF16 KV、FP8 KV、TRT-LLM-NVFP4等基线：NVFP4版本平均精度损失<0.5个点，MXFP4版本<1个点，精度优于FP8 KV；NVIDIA B300 GPU上解码kernel最高加速2.99倍，端到端服务吞吐提升2.4~3.0倍，KV缓存容量最高压缩3.5倍；RL训练rollout场景下精度与BF16 KV几乎对齐，无明显退化。
### 核心结论
算法系统协同设计的FP4 KV缓存量化可实现几乎无损的精度和数倍吞吐提升，是Blackwell架构GPU上LLM服务的核心优化方向。
