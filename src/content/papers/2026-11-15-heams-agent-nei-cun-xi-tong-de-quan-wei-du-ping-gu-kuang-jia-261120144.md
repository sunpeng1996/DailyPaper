---
title: 'HEAMS: Holistic Evaluation of Agent Memory Systems'
title_zh: HEAMS：Agent 内存系统的全维度评估框架
authors:
- Chirag Goel
- Jacob Lavoie
- Amirhossein Naghshzan
- Jordan Bannister
- Marzia Nouri
- Mehar Bhatia
- Matt Harris
- Siva Reddy
- Arsène Fansi Tchango
- Gaétan Marceau Caron
affiliations:
- Mila – Quebec AI Institute
- Mozilla
arxiv_id: '2611.20144'
url: https://arxiv.org/abs/2611.20144
pdf_url: https://arxiv.org/pdf/2611.20144
published: '2026-11-15'
collected: '2026-11-17'
category: Agent
direction: Agent 内存系统全维度评测
tags:
- Agent Memory
- Evaluation Framework
- Privacy
- Security
- User Sovereignty
- Governance Layer
one_liner: 开源Agent内存全维度评测框架，覆盖性能、效率、安全、隐私、用户主权五大维度
practical_value: '- 搭建电商导购、用户个性化服务类Agent时，不能仅验证记忆召回准确率，需同步评估隐私泄露率、用户记忆删除/修改指令响应准确率、抗投毒能力，避免只看性能忽略合规风险

  - 可复用HEAMS的可插拔治理层设计，在现有RAG/用户记忆系统外层增加独立的retention/recall策略层，无需修改底层记忆系统即可实现隐私管控，比如配置"不泄露用户历史消费敏感信息"的召回拦截策略，实测可降低约50%的隐私泄露率，仅损失不到5%的响应有用性

  - 记忆系统选型可参考实验结论：短会话场景优先用in-context记忆，性能最优；长会话（跨session用户偏好记忆）场景选HippoRAG/MilaMem这类带语义检索的方案，准确率比in-context高30%左右；隐私要求高的场景优先选带独立治理层的方案'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Agent内存系统仅围绕任务性能、效率做评测，忽略了记忆持久化带来的隐私泄露、用户修改/删除记忆指令不生效、恶意内容投毒等风险，无法支撑C端个性化Agent（如电商导购、私人助手）的合规上线需求，亟需全维度评测体系暴露不同维度的权衡关系。
### 方法关键点
- 明确Agent内存系统五大责任维度：性能、效率、隐私、用户主权、安全，拆解为可量化的行为指标
- 搭建10个基准测试集：包含5个公开性能benchmark（LoCoMo、LongMemEval等）、4个新增隐私/用户主权benchmark（上下文合规、可编辑可删除、留存策略合规、透明度）、1个安全benchmark（MPBench抗投毒）
- 设计统一内存操作接口（retain/recall/delete/consolidate），支持接入任意第三方内存系统；新增可插拔治理层，可独立配置留存、召回策略，无需修改底层内存系统
### 关键结果
对比7种内存方案（无内存、in-context、Mem0、Letta、HippoRAG、MilaMem、MilaMem+治理层）：
- 性能层面：短会话场景in-context记忆准确率最优，长会话（100K+ token）场景下，语义检索类内存系统比in-context准确率高30pct左右
- 隐私层面：无治理的内存系统最高有71.74%的响应存在隐私泄露，加召回治理层后泄露率降至31.82%，仅损失4.8pct的响应有用性，无泄漏且有用的响应占比提升15pct
- 无任何内存系统在所有维度表现最优，高性能往往伴随较差的隐私、安全表现

Agent内存系统不仅是提升任务性能的工具，更是用户持久化信息的保管者，仅测性能的评测体系完全无法覆盖合规与用户权益风险。
