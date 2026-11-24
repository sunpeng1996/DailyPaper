---
title: 'KernelShift: Benchmarking Kernel Optimization Across Evolving Hardware'
title_zh: KernelShift：面向演进硬件的内核优化编码Agent基准测试框架
authors:
- Shuaiwei Huang
- Weihua Du
- Allen Wu
- Ivan Fox
- Manupa Karunaratne
- Yiming Yang
- Sean Welleck
affiliations:
- Carnegie Mellon University
- Arm Ltd.
arxiv_id: '2611.29590'
url: https://arxiv.org/abs/2611.29590
pdf_url: https://arxiv.org/pdf/2611.29590
published: '2026-11-21'
collected: '2026-11-24'
category: Agent
direction: 编码Agent · 硬件感知内核优化评测
tags:
- Coding Agent
- Kernel Optimization
- Benchmark
- ISA Adaptation
- LLM Code Generation
one_liner: 构建跨Arm架构演进的编码Agent内核优化基准，实测Agent对新指令集的适配能力
practical_value: '- 对于LLM服务部署团队，可直接复用「Agent迭代优化+硬件在环反馈」的流程，针对业务部署的Arm架构（如Graviton系列）优化gemm、rmsnorm等核心算子，无需手动调优即可获得1.3~1.6x的prefill阶段推理提速

  - 开发代码优化类Agent的团队，可参考其极简工具链设计：仅提供compile、evaluate、disassemble三个基础工具配合迭代闭环，就能实现高效的性能优化，无需复杂的工具集开发

  - 面对新硬件/新编程范式的代码生成场景，可直接复用prompt优化技巧：在系统提示中补充新指令集的常见坑点与失败示例，即可将Agent的优化性能提升1倍'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前AI推理部署跨多硬件架构，CPU指令集（ISA）持续迭代，手动优化内核的人力成本极高。编码Agent已开始应用于内核优化，但现有基准均针对固定硬件设计，无法评估Agent随硬件演进而自适应优化的能力，亟需标准化评测体系衡量该场景下Agent的能力边界。
### 方法关键点
- 搭建Agent辅助、人工校验的基准生成流水线，从ncnn、llama.cpp、Arm SIMD Loops、KleidiAI四个开源生产库中提取99个真实内核，覆盖CV、LLM推理等场景，配套1.6k个真实业务负载。
- 设计硬件在环的统一评测环境，对Agent仅暴露compile、evaluate、disassemble三个工具，支持跨Arm Neon/SVE/SVE2/SME2四代架构评测，Agent可迭代获取硬件的正确性、性能反馈优化代码。
- 采用Speedup@40作为核心指标：即40次工具调用内生成的正确代码，相对于同硬件下专家优化内核的几何平均加速比。
### 关键实验结果
对比基线包括编译器自动向量化代码、ncnn/llama.cpp等生产级内核、Arm专家手写KleidiAI内核：
1. 成熟SVE架构下，Agent生成代码比自动向量化编译器快2.4~19.8x，比ncnn Neon内核最高快2.74x；
2. 端到端llama.cpp推理场景中，Agent优化的内核可实现1.3~1.6x的prefill阶段提速，decode阶段提速1.04~1.1x；
3. 针对需要全新编程模型的SME2架构，Agent性能仅为专家内核的0.08~0.56x，适配能力明显不足。

> 最值得记住的结论：编码Agent在成熟指令集上已经能超越普通生产级内核的优化水平，但对于需要全新编程范式的新硬件，其适配能力仍有显著瓶颈，补充场景坑点的prompt工程可大幅提升新场景下的性能
