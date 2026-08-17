---
title: 'PACE-Bench: Benchmarking Physics Adaptation via Code Evolution in Dynamic
  Environments'
title_zh: PACE-Bench：面向动态环境物理适配的自进化Agent评测基准
authors:
- Yuhao Zhan
- Bingxiang He
- Zecong Tang
- Chaojun Xiao
affiliations:
- Tsinghua University
- Zhejiang University
arxiv_id: '2608.14441'
url: https://arxiv.org/abs/2608.14441
pdf_url: https://arxiv.org/pdf/2608.14441
published: '2026-08-14'
collected: '2026-08-17'
category: Agent
direction: 自进化Agent 动态环境适配评测
tags:
- Self-Evolving Agent
- Benchmark
- Code Agent
- Dynamic Adaptation
- LLM Agent
one_liner: 提出含144组物理环境突变任务的评测基准，验证自进化Agent动态适配能力远未饱和
practical_value: '- 业务Agent鲁棒性评测可借鉴「源环境可行→环境突变失效→适配新环境」的范式，模拟线上规则/流量分布突变（如电商大促、平台政策调整）场景下的Agent适配能力

  - 自进化Agent方法选型参考：优先选择Reflexion这类带真实环境反馈校验的反思范式，避免Self-Refine这类无外部校验的自修订（易累积错误）；追求效率优先可选ToT范式，成本收益比更高

  - 动态环境下的Agent迭代不要过度依赖历史记忆锚定：记忆增强方法在环境突变后反而会限制大模型的推理能力，需平衡历史经验复用和新环境适配的权重，比如大促后不要直接复用旧策略记忆

  - 环境变化适配的核心瓶颈是机制重构而非参数识别：不要仅做参数层面的调整，要给Agent留出机制层面的迭代入口'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有自进化Agent评测均基于固定执行环境，未覆盖「原有可行方案因环境突变失效」的场景，而真实部署中环境规则、分布频繁变化是普遍情况，缺乏统一基准评测Agent的动态适配能力。

### 方法关键点
- 覆盖静力学、动力学等6个物理域共36个基础任务，每个任务对应1个源环境+4个梯度难度的突变目标环境，共144组源-目标适配对，要求Agent基于仿真诊断反馈在20次尝试内将源环境可行的代码方案适配到目标环境
- 统一评测4大类共10种主流自进化方法：上下文修订类（Reflexion、Self-Refine）、记忆增强类（ACE、ExpeL等）、推理搜索类（ToT、CodeEvolve）、参数微调类（SEAL、RAGEN等）
- 设计隐藏/暴露环境变化参数两类对照场景，区分「识别变化是什么」和「基于变化重构方案」两类能力的瓶颈

### 关键结果
- 全基准上最优配置Reflexion+Qwen3-14B的Pass@2仅35.9%，Statics子集上GPT-5.5的Pass@2也仅66.7%，基准远未饱和
- 暴露环境变化参数并未提升性能天花板，说明核心瓶颈是机制重构能力而非识别变化的能力
- 效率对比上ToT范式的Score/Hr为所有方法最高，Self-Refine因无校验内循环，效率仅为Reflexion的1/7左右

**最值得记住的一句话**：自进化Agent在动态环境下的核心瓶颈是「知道怎么改」的机制重构能力，而非「知道什么变了」的参数识别能力。
