---
title: 'Setup Complete, Now You Are Compromised: Weaponizing Setup Instructions Against
  AI Coding Agents'
title_zh: 安装完成即失陷：针对AI编码Agent的安装说明投毒攻击
authors:
- Aadesh Bagmar
- Pushkar Saraf
affiliations:
- Microsoft
arxiv_id: '2607.15143'
url: https://arxiv.org/abs/2607.15143
pdf_url: https://arxiv.org/pdf/2607.15143
published: '2026-07-16'
collected: '2026-07-18'
category: Agent
direction: AI编码Agent 供应链安全攻防
tags:
- AI Coding Agent
- Supply Chain Attack
- Dependency Installation
- LLM Security
- Agent Security
one_liner: 首次系统评估通过项目安装文档发起的AI编码代理供应链攻击并验证有效防御手段
practical_value: '- 若业务部署了自主执行工具调用/依赖安装的Agent，必须在执行前加确定性校验层，对依赖名称、源、版本做白名单校验，不要依赖LLM本身的安全识别能力

  - 给Agent的安全提示词仅能覆盖指定维度的风险，不能作为唯一安全手段，需和前置校验逻辑配合

  - 开发Agent执行框架时，不要完全信任输入的文档/指令内容，对外部依赖、跳转源等敏感操作必须做沙箱隔离+二次校验

  - 涉及第三方库安装的Agent场景，需针对不同包管理生态（pip/npm/Cargo）做差异化的风险校验规则，避免分隔符混淆类投毒绕过'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
AI编码Agent执行项目安装时直接读取文档中的依赖配置，不校验名称、来源、已知漏洞，攻击者仅修改README/requirements/Makefile即可发起供应链攻击，此前无系统性评估。
### 方法关键点
覆盖5类攻击场景、12种具体攻击向量，跨主流生产级编码Agent harness与前沿LLM开展测试，对比模型单独能力、harness+模型组合的安全表现，验证安全提示词、前置确定性校验两种方案的防御效果。
### 关键结果
- 明显typosquats攻击检测准确率接近100%，但分隔符混淆类攻击（如azurecore冒充azure-core）漏过率随harness+模型配对差异可达30%以上；
- 源重定向类攻击在npm/Cargo生态下几乎全部漏过，近100%的Agent会安装不可信依赖；
- 安全提示词仅能降低约40%对应维度的攻击成功率，而前置确定性校验可覆盖90%以上已知攻击场景。
