---
title: 'SpecPilot: Autonomous Algorithm Discovery and Systems Optimization for Speculative
  Decoding'
title_zh: 《SpecPilot：面向投机解码的自主算法发现与系统优化框架》
authors:
- Kunjun Li
- Wenhao Chai
- Yihao Liang
- Yuezhou Hu
- Shuyao Xu
- Yi Pan
- William X. Zheng
- Kannan Ramchandran
- Kurt Keutzer
- Jiantao Jiao
affiliations:
- UC Berkeley
- Princeton University
- Stanford University
- NVIDIA
arxiv_id: '2611.02501'
url: https://arxiv.org/abs/2611.02501
pdf_url: https://arxiv.org/pdf/2611.02501
published: '2026-11-01'
collected: '2026-11-04'
category: LLM
direction: LLM推理加速 · 投机解码优化
tags:
- Speculative Decoding
- LLM Inference Acceleration
- Autonomous Agent
- Lossless Weight Compression
- GPU Kernel Optimization
one_liner: 提出Agent驱动的投机解码自适应优化框架，无精度损失下解码速度较原系统提升2倍以上
practical_value: '- 可直接复用W12无损12bit权重量化方案，在单请求为主的LLM服务（如Agent调用、个性化文案生成、RAG问答）场景下，可无精度损失获得1.2x左右的AR解码速度提升，同时节省20%左右显存扩容KV缓存，承载更多并发请求

  - 落地投机解码时可参考天花板导向的瓶颈分析方法，先定位当前系统的τ、kernel效率、overhead三类瓶颈，再针对性优化，避免盲目尝试低收益优化方向

  - 可借鉴token forcing校验方法，在LLM推理优化、Agent工具调用的正确性校验场景下，避免任务精度指标漏检输出偏差，保障电商推荐文案、广告文案生成的效果一致性

  - 多Agent并行探索+结构化记忆复用的优化框架，可迁移到推荐系统线上策略调优、广告排序kernel优化等需要低风险快速迭代的场景，降低人工调优成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
投机解码是内存绑定型LLM解码的主流加速方案，但现有开源实现远未达理论上限：单请求下每步接受token数少、权重读取占比超80%，batch场景下校验开销导致加速比较单请求减半，且不同部署场景（模型、drafter、GPU、服务模式）的最优策略差异极大，手动逐场景优化成本极高，还易出现仅优化速度但改变输出的奖励黑客问题。

### 方法关键点
- 天花板导向的Agent优化循环：每轮先通过成本模型计算当前系统与理论上限的差距，定位τ（每步接受token数）、kernel效率、overhead三类瓶颈，并行Agent在多GPU上独立探索方向，仅当优化效果统计显著且输出无损才会被集成。
- 输出无损校验：设计token forcing机制，将每步输出与原系统的教师强制结果对比，仅当错配率不超过原系统0.5个百分点且无大margin错配才通过，避免任务精度指标漏检偏差。
- 结构化记忆复用：所有验证通过的优化策略（代码、效果、适用边界）存入记忆库，新部署场景可直接复用已验证策略再微调，大幅降低优化成本。
- 自主发现核心优化：包括无损W12 12bit权重格式、混合递归模型的树校验、两级校验、3种batch适配机制。

### 关键结果
在4种目标模型、3种drafter、2种GPU平台、5个基准数据集上测试，无训练、无精度损失：单请求下相对AR解码的加速比从原系统的4.46×提升到10.87×，batch场景下从1.94×提升到3.93×，所有场景下相对原系统速度提升均超2倍；W12单独用于AR解码也可获得1.19~1.28×的速度提升，同时节省14%~22%显存。

> 最值得记住的一句话：不同部署场景下投机解码的最优优化策略差异极大，天花板导向的Agent自动化探索+无损校验的框架，收益远高于单点手动优化。
