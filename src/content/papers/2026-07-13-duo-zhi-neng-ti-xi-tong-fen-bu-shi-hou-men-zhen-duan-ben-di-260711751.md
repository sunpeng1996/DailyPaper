---
title: 'When Local Monitors Miss Compositional Harm: Diagnosing Distributed Backdoors
  in Multi-Agent Systems'
title_zh: 多智能体系统分布式后门诊断：本地监控的组合危害漏检问题
authors:
- Yibo Hu
- Ren Wang
affiliations:
- Illinois Institute of Technology
arxiv_id: '2607.11751'
url: https://arxiv.org/abs/2607.11751
pdf_url: https://arxiv.org/pdf/2607.11751
published: '2026-07-13'
collected: '2026-07-14'
category: Agent
direction: 多智能体安全 · 分布式后门检测
tags:
- Multi-Agent System
- Backdoor Detection
- Runtime Safety Monitor
- Observability Boundary
- Compositional Harm
one_liner: 证明局部良性分布式后门可绕过所有本地监控，仅观测解码组装体可实现拦截
practical_value: '- 多Agent业务流程（如电商导购、自动运营）需新增组装阶段安全校验，不能仅依赖单步消息/工具调用监控，避免分布式恶意payload拆分绕过检测

  - Agent安全监控设计优先匹配危害形成的表示层：代码类危害监控解码后的可执行结构，用户侧话术类危害监控最终输出的完整文本，而非中间片段

  - 无攻击样本的安全检测可借鉴仅用良性流量训练的one-class方法，通过提取组合后的结构特征（如代码密度、可解析性）实现跨未知编码的后门检测，平均AUROC可达0.874

  - 安全监控评估需规避数据集shortcut，优先做特征消融+分布偏移测试，避免仅靠长度、熵等表层特征的监控在攻击方匹配特征后直接失效'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前多Agent、工具调用LLM系统普遍采用步级本地运行时监控，逐次检查单条消息、工具调用是否恶意，但分布式后门可将恶意payload拆分到多个Agent的输出中，每个片段本地检测都通过，组装后才产生危害，现有评估只看本地检测率，完全未覆盖这类组合危害场景，存在严重安全漏洞。

### 方法关键点
- 形式化定义**Observability Boundary**：仅当监控的观测视图能区分攻击片段与良性流量时才能检测，若满足ε-局部不可区分（攻击片段与良性流量的总变差距离≤ε），任何本地检测器的检测优势（TPR-FPR）最高不超过ε，与检测器能力无关
- 设计可控测试床，固定最终攻击payload，调整单片段的可见证据梯度，从有明显源汇边、可疑编码到完全局部良性，验证不同监控的失效边界
- 对比6类观测视图的监控能力：本地视图（污点追踪、步级统计/学习检测器）、组装视图（带标记/无标记、盲编码）、解码视图门控

### 关键实验
实验在Collaborative Shadows、AgentDojo、DemonAgent三个基准上开展：本地视图在局部良性场景下AUROC跌到接近0.5，完全失效；仅用良性数据训练的无标记组装监控跨未知编码的平均AUROC达0.874；已知编码族的解码视图门控可100%拦截所有测试攻击（ASR=0）；仅扩大观测窗口而不解码的全轨迹监控仍然失效，ASR与无防御场景一致。

### 核心结论
局部安全不等于全局安全，当危害是组合产生时，监控的核心不是观测范围有多广，而是是否触达危害形成的表示层
