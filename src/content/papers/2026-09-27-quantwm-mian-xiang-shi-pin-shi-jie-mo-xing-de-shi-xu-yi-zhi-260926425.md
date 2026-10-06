---
title: 'QuantWM: Temporally Consistent 2-Bit KV Cache Quantization for Video World
  Models'
title_zh: QuantWM：面向视频世界模型的时序一致2比特KV缓存量化框架
authors:
- Jiaqi Zhao
- Xiaobin Hu
- Bo Yin
- Junpeng Jiang
- Miao Zhang
- Shuicheng Yan
affiliations:
- Harbin Institute of Technology (Shenzhen)
- National University of Singapore
arxiv_id: '2609.26425'
url: https://arxiv.org/abs/2609.26425
pdf_url: https://arxiv.org/pdf/2609.26425
published: '2026-09-27'
collected: '2026-10-06'
category: LLM
direction: LLM推理优化 · KV cache量化
tags:
- KV Cache Quantization
- Video World Model
- 2-bit Quantization
- Training-free
- Inference Efficiency
one_liner: 提出免训练2bit KV缓存量化框架QuantWM，缓解视频世界模型量化后时序闪烁，最高实现6.20倍缓存压缩
practical_value: '- 生成式推荐/Agent对话的KV缓存量化可复用QSAC思路：结合历史Query敏感度加权选择量化质心，降低Key量化对注意力logits的扰动，避免推荐结果/对话响应跳变

  - 低比特量化后可补充PSAC机制：提取Query主成分子空间做低秩误差补偿，仅增加极小存储开销就能大幅缓解量化导致的序列一致性下降问题

  - 业务上线可复用论文的量化工程优化：流式分块量化、Triton核融合重构KV、低比特打包存储等技巧，平衡压缩率和推理延迟'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
视频世界模型依赖KV缓存存储历史时空token保证长时序一致性，但缓存随生成过程持续膨胀成为部署瓶颈；现有2bit KV量化方法虽然在通用视频基准上指标接近无损，但应用到视频世界模型时会出现严重的时序闪烁、画质下降，且发现Key量化的重构误差比Value更小，但对输出结果的负面影响远大于Value，根源是Key扰动会改变注意力logits，导致Query选择的时空token偏移。

### 方法关键点
- 量化敏感度感知聚类（QSAC）：结合历史Query二阶统计的通道敏感度、残差分组动态范围选择质心，降低对注意力logits影响大的通道的量化误差
- 主子空间注意力补偿（PSAC）：提取Query能量占比最高的前8个主方向构成低秩子空间，补偿Key量化在敏感方向的误差，稳定注意力logits
- 完全免训练，兼容现有视频生成/大模型推理架构，额外开销极低

### 关键实验
在LingBot-World-v2、HY-World 1.5等5个主流视频世界/生成模型上测试，对比SOTA基线QVG、KIVI：1. 时序token选择偏移率从平均51.55%降至15.31%；2. 最高实现6.20倍KV缓存压缩，推理延迟仅增加5%左右，部分模型因减少显存换页延迟下降17.78%；3. 480p视频上PSNR平均提升2-4dB，LPIPS平均降低30%以上，时序闪烁问题基本消除。

**最值得记住的一句话**：KV缓存量化不能只看重构误差，Key对注意力分布的影响远大于Value，保护注意力logits一致性比降低量化MSE更重要
