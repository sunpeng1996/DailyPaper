---
title: 'MemSecBench: Tracking Agent Memory Poisoning from Persistence to Consequence
  and Repair'
title_zh: MemSecBench：Agent内存投毒全链路追踪测评基准
authors:
- Xuanze Chen
- Xukang Xie
- Wentao Fu
- Jiajun Zhou
- Shanqing Yu
- Qi Xuan
affiliations:
- Zhejiang University of Technology
- Institute of Cyberspace Security, ZJUT
- Binjiang Institute of Artificial Intelligence, ZJUT
- College of Information Engineering, ZJUT
arxiv_id: '2607.27080'
url: https://arxiv.org/abs/2607.27080
pdf_url: https://arxiv.org/pdf/2607.27080
published: '2026-07-29'
collected: '2026-07-30'
category: Agent
direction: Agent 内存安全全链路测评
tags:
- LLM Agent
- Memory Poisoning
- Benchmark
- Security Evaluation
- Agent Security
one_liner: 提出Agent内存投毒全生命周期测评基准，支持多组件组合下的安全能力量化对比
practical_value: '- 电商/导购Agent安全评估可复用Write-Execute-Forget框架，测试商家上传材料、用户输入等外部内容是否会被持久化为恶意规则，后续触发错误改价、隐私泄露等风险

  - 内存后端选型参考：无通用最优内存组件，需结合自身Agent框架、LLM选型实测；高修复需求场景优先测试A-MEM类产品，其选择性修复率较原生内存最高可提41.3个百分点

  - 防御优化优先级：重点在恶意内存召回后的采纳环节加校验（如对比权威规则一致性），该环节是攻击成功的核心瓶颈；修复环节需优先保障良性内存不丢失，避免全量清内存的简单方案'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有Agent内存安全测评仅覆盖单环节，无法追踪同一份恶意语义从写入、持久化、触发危害到选择性修复的完整生命周期，也无法在控制变量下对比不同内存后端、Agent框架、LLM的安全表现，无法支撑真实业务场景的内存风险评估。

### 方法关键点
- 设计统一的Write-Execute-Forget三阶段评估协议，覆盖内存投毒全生命周期，设置7个可量化检查点，实现恶意语义的全链路追踪
- 构造310个真实场景用例，覆盖代码科研、日常生活、办公3个领域共48种上下文，每个用例明确定义目标恶意语义、需保留的良性内存、各阶段判定规则
- 采用证据驱动的裁决机制，结合确定性写入检查、checkpoint专属Judge模型评估、程序化校验，避免仅依赖Agent响应判定的误差
- 支持控制变量下的多组件对比，固定任务、初始状态、评估规则，仅替换Agent框架、内存后端、LLM即可实现横向对比

### 关键实验结果
基于24种配置组合（2种Agent框架×4种内存后端×3种LLM）测试，核心数据：
1. 全配置平均恶意内存持久化率84.2%，端到端投毒攻击成功率50.3%
2. 成功投毒的案例中，59.6%可触发实际业务危害，仅56.1%能完成选择性修复（删除恶意内容且保留所有良性内存）
3. 不同内存后端的安全表现差异极大：相比原生内存，A-MEM最高可提升41.3个百分点的选择性修复率，部分后端最高可降低16.1个百分点的端到端攻击成功率

### 核心结论
Agent内存安全是全链路问题，单独优化LLM或内存存储都不足以抵御投毒，必须覆盖写入、召回、采纳、修复全环节做体系化防御
