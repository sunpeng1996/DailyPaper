---
title: 'Beyond Maliciousness: Static and Runtime Attack-Surface Profiling of Agent
  Skills'
title_zh: Agent 技能静态与运行时攻击面分析：不局限于恶意意图检测
authors:
- Ratnesh Pandey
- Japneet Singh
- Harsh Akshit
- Sonali Tyagi
- Cassie Crossley
affiliations:
- Metano Labs
- Purdue University
- VulNow
arxiv_id: '2610.19264'
url: https://arxiv.org/abs/2610.19264
pdf_url: https://arxiv.org/pdf/2610.19264
published: '2026-10-12'
collected: '2026-10-20'
category: Agent
direction: Agent 安全 · 技能攻击面检测
tags:
- Agent Security
- Skill Profiling
- Static Analysis
- Runtime Detonation
- Permission Audit
one_liner: 提出静态分析+沙箱运行的两阶段Agent技能攻击面检测方法，量化权限声明偏差与非恶意暴露风险
practical_value: '- 搭建内部Agent技能市场时，不可依赖开发者主动声明的权限，必须强制走静态扫描+无前置筛选沙箱运行的双阶段校验，实测77%的权限声明与实际能力不符，59%存在少报

  - 电商/推荐场景引入第三方Agent技能（如竞品爬虫、营销文案生成工具）时，上线前必须检测shell执行、文件读写、网络外发、凭据访问4类高危能力，70%的技能至少携带1项高权限

  - 自研Agent权限体系可直接复用本文的能力分级规则，将shell执行、凭据访问设为默认禁止的高危权限，运行时动态拦截，避免使用仅移除确认提示的弱权限模型'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent技能安全检测仅聚焦恶意意图识别，忽略了无恶意的技能也会因权限过大扩大攻击面；当前技能权限声明机制几乎失效，开发者上报的权限与实际能力偏差极大，用户安装时完全感知不到隐藏风险。

### 方法关键点
- 两阶段检测框架：先对技能完整包做静态分析，检查硬编码密钥、依赖溯源、能力匹配；再对所有样本无前置筛选直接放入sandbox运行，记录进程、工具调用、网络活动，用独立的Judge LLM评估运行轨迹
- 三维度独立检测：将结果拆分为恶意意图（Threat）、暴露风险（Risk）、能力 footprint（Attack Surface）三个独立维度，互不干扰计算，避免风险被恶意意图检测漏判
- 权限声明校验：对比开发者在frontmatter中声明的权限与静态+运行时检测到的实际能力，统计偏差率与偏差方向

### 关键结果
测试集覆盖两个公开Agent技能市场的6309个中腰部流行度技能，核心数据：70%的技能至少携带1项高权限，50%支持shell执行，35%可读取文件、31%可写入文件/发起网络外发、13%可访问凭据；仅12.7%的技能声明了权限，其中59%的声明少报实际能力，ClawHub平台88%的声明存在少报。仅5.4%的技能存在恶意意图，但25.7%的技能属于高暴露风险，其中80%的高风险技能无任何恶意特征。

### 最值得记住的结论
Agent技能的安全防护不能只排查恶意特征，70%的攻击面来自无恶意但权限过大的合法技能，依赖开发者主动上报权限完全不可靠
