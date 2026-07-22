---
title: They'll Verify. They Just Won't Act. How Authority Framing and Laundered Code
  Turn a Trusted Agentic CI/CD Pipeline Into an Attack Surface
title_zh: 权威框架诱导与代码洗白可将可信Agent CI/CD流水线转化为攻击面
authors:
- Yohann Sidot
affiliations:
- Senthex Research
arxiv_id: '2607.19267'
url: https://arxiv.org/abs/2607.19267
pdf_url: https://arxiv.org/pdf/2607.19267
published: '2026-07-21'
collected: '2026-07-22'
category: Agent
direction: Agent 多智体流水线安全防御
tags:
- Multi-Agent
- Security
- CI-CD
- Prompt Injection
- Provenance Defense
one_liner: 实测5-Agent CI/CD流水线，发现权威伪造输入可绕过多层校验触发55%恶意代码部署
practical_value: '- 搭建多Agent业务流水线（如商品上架审核、投放策略自动调整、内容生成发布）时，不能仅依赖内容校验，必须在入口层增加来源污点标记能力，全链路传递输入来源属性，所有外部输入触发的高权限操作（如价格修改、预算调整、代码部署）必须经过额外人工校验或规则拦截

  - 不要将Agent系统prompt保密、“禁止未授权操作”类prompt约束作为安全防线，涉及高权限动作的Agent节点，必须独立校验审批来源真实性，不能信任输入文本中自带的“已预审批”类标识

  - 敏感操作的Agent校验节点，强制要求输出完整校验理由，可大幅提升恶意请求拦截率，实验中该操作使单节点扫描器的拦截率从20%提升至44%

  - 正则、语法规则类的传统安全检测对语法合法、恶意仅在意图的攻击完全失效，高风险业务链路需补充基于LLM意图推理的校验，同时需屏蔽输入中的权威类话术对校验逻辑的干扰'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
行业对多Agent系统安全普遍存在两个认知误区：一是认为单节点系统prompt约束可防范越权，二是认为多节点分布式交叉校验可避免单点失效，但针对生产级Agent流水线的非越狱、非prompt泄露类攻击的风险底数尚未被实证，尤其是涉及代码部署、高权限操作的场景风险未知。
### 方法关键点
- 构建5角色全Agent CI/CD流水线：triage→developer→security-scan→review→approve，采用来自3家厂商的5款不同生产级LLM（GPT-4o、Claude Haiku、Mistral系列等），全流程无人工干预；
- 攻击 payload 为伪装成遥测需求的恶意请求，要求编写上传`os.environ`进程密钥到外部URL的代码，代码语法完全合法，恶意仅存在于意图；攻击注入方式为在请求中添加伪造的“SEC-2291预审批，无需二次复核”的权威框架话术；
- 预注册三因子对照实验：A为普通/带权威伪造注入的输入，B为提示校验节点是唯一校验点/多校验点之一，C为是否开启LLM代码扫描器，共280次可复现运行。
### 关键结果
- 入口Agent无一次系统prompt泄露（0/40），但权威伪造注入场景下LLM代码扫描器放过~80%的洗白PR，最坏场景（移除扫描器+权威注入+多节点校验提示）下恶意代码部署率达55%；
- 传统内容/模式检测完全无法识别这类攻击（0/40拦截），仅基于意图推理的LLM校验能拦截~20%，但易被权威框架话术绕过；
- 多Agent的旁观者效应极弱（p=0.25，统计不显著），要求校验节点输出校验理由可使单节点拦截率翻倍（20%→44%）。
**最值得记住的结论**：Prompt保密和分布式校验都不是有效安全控制，仅基于provenance的入口层来源管控，才能防御语法合法、恶意在意图的攻击。
