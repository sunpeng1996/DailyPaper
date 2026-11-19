---
title: 'RSIBench-Infra: Can Agents Optimize Their Own Training and Inference Infrastructure
  at Production Scale?'
title_zh: RSIBench-Infra：面向生产级规模的Agent自优化训练推理基准
authors:
- Hanlin Wu
- Yifei Wang
- Zhicheng Cai
- Huan-ang Gao
- Wei-Ying Ma
- Ya-Qin Zhang
- Jingjing Liu
- Hao Zhou
affiliations:
- ByteDance Seed
- Institute for AI Industry Research (AIR), Tsinghua University
- SIA-Lab of Tsinghua AIR and ByteDance Seed
arxiv_id: '2611.24395'
url: https://arxiv.org/abs/2611.24395
pdf_url: https://arxiv.org/pdf/2611.24395
published: '2026-11-18'
collected: '2026-11-19'
category: Agent
direction: Agent 生产级基础设施性能优化
tags:
- Agent
- Infrastructure Optimization
- Benchmark
- Recursive Self-Improvement
- LLM Serving
one_liner: 首个支持Agent跨软件栈优化生产级训练推理性能的标准化基准套件
practical_value: '- 电商/推荐场景LLM服务性能优化可优先落地文中验证的高ROI方向：KV cache扩容、算子融合、图编译、投机解码，四类优化有效率均超75%，可快速降低推理成本

  - 大模型训练/推理优化的验收流程可参考OCI分层提交+独立质量校验+端到端性能评估的方案，避免局部优化不生效、优化导致业务效果下降的问题

  - 业务侧做Agent选型时可参考成本-效率曲线：GPT-6 Astra性能最优，DeepSeek/GLM在成本仅为前者1/10的情况下可达到70%的优化成功率，性价比更高'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前全球AI基础设施投入预计2026年达4870亿美元，但主流LLM服务引擎仅能达到理论最优吞吐的22%~38%，算力浪费严重。现有Agent驱动的性能优化基准仅聚焦内核等单一软件层，无法验证生产场景下跨栈优化的端到端收益，同时递归自提升（RSI）的迭代循环也依赖更高效率的训练推理栈支撑。

### 方法关键点
- 构建20个生产级任务集，覆盖16类推理（文本、多模态、视频生成、TTS等，参数量1.7B~2.8T）、4类训练（SFT、GRPO、蒸馏等）任务，适配NVIDIA GPU、昇腾NPU，最大支持32卡分布式部署
- 允许Agent跨引擎、内核、指令三层优化软件栈，采用OCI镜像层作为统一提交协议，完整捕获所有修改实现可复现部署
- 设计独立校验流程：优化部署与性能/质量评估完全隔离，性能收益仅在通过任务专属质量门（效果不下降）后生效，杜绝基准作弊

### 关键结果
测试7种Agent配置，130个有效提交中66.2%的优化取得1.10x以上的有效加速：GPT-6 Astra在全20任务上Faster Rate达80%，中位加速比1.33x；Claude Opus 5.5在10个任务上中位加速比达1.34x。验证得到Top3高成功率优化方向：投机解码/MTP（95.7%）、图编译（88.6%）、缓存/内存优化（79.5%）。

### 核心结论
当前Agent已经可以落地生产级训练推理性能优化，优先选择高ROI跨栈优化方向，可在不损失业务效果的前提下降低30%以上的计算成本。
