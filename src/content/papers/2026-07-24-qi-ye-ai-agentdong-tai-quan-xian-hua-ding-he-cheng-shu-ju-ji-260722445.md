---
title: 'Dynamic Capability Scoping for Enterprise AI Agents: A Synthetic Dataset and
  Three-Source Permission Architecture'
title_zh: 企业AI Agent动态权限划定：合成数据集与三源权限架构
authors:
- Halil Burak Noyan
affiliations:
- Independent Researcher, London, UK
arxiv_id: '2607.22445'
url: https://arxiv.org/abs/2607.22445
pdf_url: https://arxiv.org/pdf/2607.22445
published: '2026-07-24'
collected: '2026-07-27'
category: Agent
direction: Agent 企业级安全权限管控
tags:
- LLM Agent
- Dynamic Permission
- Enterprise AI
- Synthetic Dataset
- Security Architecture
one_liner: 提出动态最小权限三源架构，配套600条企业任务标注数据集，降低Agent过权限攻击面
practical_value: '- 电商内部Agent（运营数据分析、客服工单处理等）可直接复用三源权限架构：先设角色权限天花板、再根据任务预测最小权限、最后禁止高风险权限组合（如数据库读+外部发邮件/HTTP请求），从根源降低用户数据泄露风险

  - 可借鉴两通合成数据集生成方法：先基于业务场景生成任务prompt，再独立标注权限标签避免循环偏差，同时可通过生成的任务反哺迭代内部权限政策，减少政策与实际业务的gap

  - 权限分类器可采用非对称置信阈值：高风险权限（用户数据导出、外部消息推送等）要求高置信才授予，低风险权限（内部知识库读等）放宽阈值，平衡安全与业务体验

  - 可先采用观察模式部署权限管控：先不拦截，仅记录Agent权限调用与预测结果的差异，积累业务数据后再切强制模式，避免上线初期影响正常流程'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
企业AI Agent部署时普遍静态授予全量角色权限，与单任务实际所需权限存在错配，过度授权大幅放大攻击面；现有权限管控多为事后检测拦截，面对具备对齐伪造、逃逸检测能力的Agent存在结构性防护上限，需从根源减少可用权限降低风险。

### 方法关键点
- 三源权限架构：1. 角色权限天花板：根据Agent所属部门/身份预定义最大权限集合，纯规则无推理作为硬上限；2. 任务上下文分类器：基于用户输入的任务描述独立预测当前任务所需最小权限，不受Agent本身影响，不同风险等级权限采用非对称置信阈值；3. 政策级组合禁令：禁止高风险权限组合（如私有数据访问+外部通信+不可信内容访问的致命三重组合），从结构上杜绝间接prompt注入导致的数据泄露
- 合成数据集采用两通生成管线：Pass1仅基于企业多部门政策生成任务prompt（无权限标签知识），Pass2独立标注每条任务对应的15种工具权限的最小集合，避免循环偏差，同时通过数据集迭代反哺优化权限政策

### 关键结果
- 600条标注数据集10%样本人工校验，预评审Cohen's κ=0.917，争议解决后κ=0.967，达到几乎完美一致性；权限标注精确匹配率85%，汉明准确率98.8%，风险加权过度授权率下降86.7%
- 数据集与政策迭代后，权限天花板违规数从46降至3，降幅93%

**最值得记住的一句话**：Agent上下文里不存在的凭证，无论Agent的推理或逃逸能力多强，都无法被滥用
