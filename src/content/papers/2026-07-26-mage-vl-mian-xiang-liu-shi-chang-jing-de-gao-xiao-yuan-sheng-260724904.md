---
title: 'Mage-VL: An Efficient Codec-Native Streaming Multimodal Foundation Model'
title_zh: Mage-VL：面向流式场景的高效原生编解码多模态基础模型
authors:
- Senqiao Yang
- Kaichen Zhang
- Zhaoyang Jia
- Jinghao Guo
- Yifei Shen
- Xinjie Zhang
- Xiaoyi Zhang
- Haoqing Wang
- Xiao Li
- Peng Zhang
affiliations:
- Microsoft Mage Team
arxiv_id: '2607.24904'
url: https://arxiv.org/abs/2607.24904
pdf_url: https://arxiv.org/pdf/2607.24904
published: '2026-07-26'
collected: '2026-07-29'
category: Multimodal
direction: 多模态基础模型 · 流式视频推理优化
tags:
- VLM
- Streaming Perception
- Video Understanding
- Codec Acceleration
- Multimodal Foundation Model
one_liner: 提出原生编解码架构的流式多模态模型，推理速度最高3.5倍，性能优于同/更大规模基线
practical_value: '- 短视频推荐/直播理解场景可复用Mage-ViT的动态区域编码思路，仅编码高熵运动区域，降低75%以上视觉token计算量，提升推理效率

  - 实时多模态Agent交互场景可借鉴双系统架构，轻量事件门过滤无效流数据，按需触发大模型推理，降低端侧/在线部署成本

  - 多模态模型训练可复用AI4AI数据流水线方案，通过prompt-code联合优化、AI驱动性能诊断，提升训练效率减少标注依赖'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有VLM存在莫拉维克悖论：离线复杂视觉推理表现优异，但流式感知任务效率低、性能差，无法适配实时多模态交互场景。
### 方法关键点
1. 自研Mage-ViT视觉tokenizer：替换均匀帧采样，跨I/P帧利用运动向量与残差能量，选择性编码高熵动态区域，patch粒度16×16
2. 双系统架构：轻量System 1事件门做流数据过滤，因果System 2解码器做深度推理，实现主动流式感知
3. 配套AI4AI数据流水线：覆盖多模态captioning的prompt-code联合优化、AI驱动训练诊断
### 关键结果
- 视觉token消耗降低75%+，Mage-ViT仅用560M无标注图像+100M无标注视频帧预训练，性能追平百亿级图文对训练的旗舰编码器
- Mage-VL-4B静态任务持平Qwen3-VL-4B，视频理解、空间推理性能显著提升，推理速度最高3.5倍，全面超越15B Phi-4-reasoning-vision基线
