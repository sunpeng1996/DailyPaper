---
title: 'AscendGYM: A Cost-Aware Kernel Optimization Benchmark for Real-World Workloads
  on Ascend NPUs'
title_zh: AscendGYM：面向昇腾NPU真实负载的成本感知Kernel优化基准
authors:
- AI Training Platform Team
- Bingwei Zhang
- Jing Li
- Amir Abdullin
- Sihang Chen
- Xin Chen
- Liangjun Feng
- Yingmeng Gao
- Tao Guo
- Junjie Huang
affiliations:
- Shenzhen Loop Area Institute
- SLAI AI Training Platform Team
arxiv_id: '2611.17621'
url: https://arxiv.org/abs/2611.17621
pdf_url: https://arxiv.org/pdf/2611.17621
published: '2026-11-12'
collected: '2026-11-18'
category: Agent
direction: Agent 代码优化基准测试
tags:
- Agent
- Benchmark
- Kernel Optimization
- Ascend NPU
- LLM Coding
one_liner: 提出面向昇腾NPU真实负载的Kernel优化基准，引入成本感知STS指标评估代码Agent优化能力
practical_value: '- 自研代码Agent做算子优化的团队，可直接复用AscendGYM的48个真实负载Kernel任务集、AscendForge沙箱环境，快速搭建验证pipeline，降低基准构建成本

  - 评估代码Agent优化效率时，可复用STS指标设计，同时考量最终加速比和token消耗，平衡优化收益与成本，避免无意义的资源浪费

  - 昇腾NPU上部署LLM/生成式推荐服务的团队，可直接引入AscendGYM已验证的优化后Kernel，提升Attention、RMSNorm等核心算子性能，降低推理时延与算力成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有昇腾NPU的Kernel基准多聚焦从0生成算子的能力，未覆盖基于真实业务负载的输入配置优化已有实现的场景，也未考虑Agent优化过程的token、时间等资源成本，评估结果无法直接反映优化方案的实际落地价值。
### 方法关键点
- 任务集包含48个来自真实LLM训练/推理负载的Kernel，分3个难度等级，完全保留真实业务中的张量形状、数据类型、执行上下文，测得的优化收益可直接映射到对应业务的性能提升
- 内置AscendForge沙箱，统一提供代码编译、正确性校验、性能测试、迭代反馈能力，屏蔽昇腾NPU底层部署细节，适配Agent的迭代优化流程
- 提出STS（Speedup-Token Score）指标，加权计算最终加速比和优化过程的累计token消耗，同时惩罚优化收益的延迟获取，更合理评估预算约束下的优化效率
- 支持两种评估模式：固定内置harness比对不同LLM的Kernel优化能力，以及端到端评估自定义代码Agent系统的完整性能
### 关键结果
在17个入门难度任务上测试18种主流LLM+harness组合，70%的组合几何平均加速比低于1.2x，说明当前代码Agent对已有Kernel的优化空间仍很大；Claude Code + Claude Opus 5组合在50M token预算下实现最高1.69x几何平均加速比，部分Kernel最大加速比达3.29x。
### 最值得记住的一句话
Kernel优化评估不能仅看最终加速比，必须结合实际业务负载配置和资源成本，才能筛选出可落地的高性价比优化方案。
