---
title: 'ReactVAU: A Slow-Fast Decoupled Framework for Streaming Video Anomaly Understanding'
title_zh: ReactVAU：面向流视频异常理解的快慢解耦框架
authors:
- Chia-Hui Chen
- Shih-Ying Yeh
- Fu-En Yang
- Min-Hung Chen
- Shang-Hong Lai
affiliations:
- National Tsing Hua University
- NVIDIA
arxiv_id: '2609.07941'
url: https://arxiv.org/abs/2609.07941
pdf_url: https://arxiv.org/pdf/2609.07941
published: '2026-09-06'
collected: '2026-09-10'
category: Multimodal
direction: 多模态大模型·流视频异常推理
tags:
- MLLM
- Streaming Video
- Memory Mechanism
- Anomaly Detection
- Slow-Fast Architecture
one_liner: 提出快慢解耦的流视频异常理解框架，轻量过滤触发大模型推理，兼顾效果与效率
practical_value: '- 可复用快慢解耦架构：用轻量小模型做前置触发过滤，仅高价值/异常请求调用大模型，大幅降本提效，适合电商实时风控、推荐触发式大模型文案生成场景

  - 可借鉴Anomaly-Aware Persistent Memory（AAPM）设计：针对稀疏高价值信号做独立存储，避免时序压缩时丢失关键特征，可用于用户行为序列中高价值互动、异常转化信号的保留

  - 触发式大模型调用逻辑可迁移至Agent决策流：无需全链路调用大模型，仅前置模块识别到高优先级事件时唤醒大模型做语义推理，大幅降低Agent runtime开销'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视频异常理解（VAU）方法存在两类落地瓶颈：离线方法依赖全局时序采样违反因果性，无法适配直播流场景；通用流视频模型易在内存压缩时丢失稀有瞬态异常特征，且长正常时段也会高频调用高开销MLLM，计算成本极高。
### 方法关键点
提出快慢解耦框架ReactVAU，核心包含三个协同组件：
1. 基于Spatial Grid Folding（SGF）的轻量快速检测模块，做连续异常预过滤
2. Anomaly-Aware Persistent Memory（AAPM），保护关键视觉特征不随时序衰减丢失
3. 重载慢速推理模块，正常流时段休眠，仅被可疑事件唤醒做语义验证与因果描述
### 关键结果
在严格满足流场景因果约束的前提下，异常检测与因果推理性能达同期SOTA水平，通过最小化MLLM调用次数，计算效率实现量级提升
