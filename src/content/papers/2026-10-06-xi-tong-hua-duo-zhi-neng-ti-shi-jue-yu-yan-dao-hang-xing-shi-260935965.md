---
title: 'Systematic Multi-Agent Vision-and-Language Navigation: Formulation, Benchmark,
  and Method'
title_zh: 系统化多智能体视觉语言导航：形式化定义、基准与方法
authors:
- Yunzhe Xu
- Zhe Liu
affiliations:
- Shanghai Jiao Tong University
arxiv_id: '2609.35965'
url: https://arxiv.org/abs/2609.35965
pdf_url: https://arxiv.org/pdf/2609.35965
published: '2026-10-06'
collected: '2026-10-13'
category: MultiAgent
direction: 多智能体具身导航 · LLM调度与共享记忆
tags:
- MultiAgent
- VLN
- LLM Planning
- Shared Memory
- Benchmark
- Embodied AI
one_liner: 提出首个带依赖资源约束的多智能体VLN基准MAVLN与基线系统TRISS
practical_value: '- 多智能体任务调度可复用LLM预分配+等待触发机制：将依赖等待与任务执行并行，降低整体链路耗时，可直接迁移至多Agent协同的电商用户运营、订单履约调度场景

  - 多智能体共享记忆可复用带校验的全局拓扑归并机制：所有Agent的探索结果实时共享，避免重复劳动，适合推荐系统多Agent协同挖掘用户意图、全域商家标签体系构建场景

  - 多智能体并行执行可复用两段式冲突解决框架：先通过匈牙利算法做冲突-free目标分配，再做时空路径搜索规避运行时碰撞，可优化广告多预算约束下的流量分配、大促资源调度的冲突率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多智能体视觉语言导航（VLN）范式存在两大缺陷：一是任务约束过简，仅支持链式依赖、无资源冲突度量，与真实场景需求脱节；二是LLM驱动的多智能体规划依赖预构建环境、模拟器API，无法适配未知环境，缺乏系统化的任务定义与通用基准。

### 方法关键点
- 形式化定义多智能体VLN为带DAG子任务依赖、持有链、存在锁三类约束的协调问题，构建四阶段自动化任务生成管线，产出MAVLN基准，包含11724个episode、145个场景、最多4个智能体、三种指令模式
- 提出基线系统TRISS：1）LLM子任务调度器，自动识别约束并动态分配原子指令，支持预分配+触发机制并行等待与执行；2）全局共享拓扑记忆，所有智能体的探索结果实时归并复用；3）冲突感知执行机制，通过匈牙利算法做目标分配、冲突搜索做路径规划，避免碰撞
- 设计约束感知的评估指标体系，覆盖任务成功率、路径效率、执行冲突率等维度

### 关键结果
- Oracle调度+导航配置下可实现100%任务成功率，相比单智能体执行耗时降低47.8%，验证多智能体协作的并行收益
- TRISS在测试集上任务成功率达9.3%，相比随机调度、顺序调度分别提升45.5倍、3.7倍，相比单智能体版本成功率提升57.6%
- 消融实验显示：启用共享记忆可提升成功率46.8%，冲突解决机制可降低智能体冲突率63.6%

> 最值得记住：多智能体系统的核心收益来自任务并行，而核心瓶颈依次是调度约束理解、规划精度、执行冲突解决，三者缺一不可
