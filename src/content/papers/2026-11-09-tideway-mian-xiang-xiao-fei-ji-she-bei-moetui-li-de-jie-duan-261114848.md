---
title: 'Tideway: Phase-Aware Tiered Memory Management for MoE Inference on Consumer
  Devices'
title_zh: Tideway：面向消费级设备MoE推理的阶段感知分层内存管理系统
authors:
- Yifei Wang
- Tsun-yu Yang
- Yechen Xu
- Hancheng Ye
- Qinsi Wang
- Baijun Zhou
- Tingjun Chen
- Hai &#34;Helen&#34; Li
- Danyang Zhuo
- Yiran Chen
affiliations:
- Duke University
arxiv_id: '2611.14848'
url: https://arxiv.org/abs/2611.14848
pdf_url: https://arxiv.org/pdf/2611.14848
published: '2026-11-09'
collected: '2026-11-19'
category: LLM
direction: LLM推理 · 消费级设备MoE内存优化
tags:
- MoE
- Inference Optimization
- Tiered Memory
- Consumer Device
- CUDA Graph
one_liner: 通过统一内存池与阶段感知优化，实现消费级设备上MoE推理平均1.97倍端到端提速
practical_value: '- 部署端侧电商导购Agent等场景可直接复用Tideway架构，解决大MoE模型在消费级GPU上的部署难题，降低硬件成本

  - 线上MoE推荐/大模型推理服务可迁移阶段感知布局思路，针对prefill、decode不同访存pattern动态调整缓存策略，降低TTFT、TPOT

  - 动态分页场景下可复用分段CUDA Graph捕获方法，保留图执行低开销优势，避免eager执行的kernel launch损耗'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前MoE模型因低激活算力成本成为端侧Agent的核心选型，但消费级设备GPU VRAM、主机RAM容量有限，大模型权重需在VRAM、RAM、SSD间溢出存储。现有系统将分层内存视为独立缓存，导致推理时频繁抖动，TTFT、TPOT过高，无法支撑流畅的端侧交互。
### 方法关键点
- 统一内存池设计：将VRAM、RAM合并为统一内存池，SSD作为后备存储，跨层去重专家副本，最大化有效内存容量，减少SSD读写
- 阶段感知内存布局：针对prefill阶段全量专家访问、decode阶段稀疏专家访问的差异动态切换布局，prefill锚定RAM可复用专家避免被刷除，decode回收VRAM的prefill缓存作为专家槽位
- 副本感知替换策略：VRAM淘汰的专家优先回写RAM而非直接丢弃，懒回收跨层重复副本，进一步减少SSD加载
- 分页感知执行引擎：prefill用双缓冲流水线重叠权值传输与计算，decode拆分CUDA Graph为可复用分段，在动态分页场景下保留图执行低开销
### 关键结果
在RTX 5090消费级GPU上测试，对比FreeToken、llama.cpp等4个SOTA基线，覆盖3个前沿MoE模型、270种静态配置、8组多轮Agent trace：平均端到端时延1.97倍提升，TTFT平均2.4倍提升，TPOT平均1.61倍提升，Agent场景最高提速3.14倍。
**最值得记住的结论**：端侧MoE推理的核心瓶颈不是算力，而是分层内存的协同利用率，针对不同推理阶段的访存特性做针对性优化可获得数倍性能提升
