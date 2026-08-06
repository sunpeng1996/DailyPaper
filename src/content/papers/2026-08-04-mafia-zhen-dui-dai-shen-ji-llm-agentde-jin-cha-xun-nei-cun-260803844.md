---
title: 'MAFIA: Query-Only Memory Attacks via Probing and Factual Injection against
  Audited LLM Agents'
title_zh: MAFIA：针对带审计LLM Agent的仅查询内存注入攻击框架
authors:
- Jiaming Chen
- Yisen Gao
- Yanping Li
- Zifan Liu
- Yumeng Zhang
- Jun Zhang
affiliations:
- The Hong Kong University of Science and Technology
arxiv_id: '2608.03844'
url: https://arxiv.org/abs/2608.03844
pdf_url: https://arxiv.org/pdf/2608.03844
published: '2026-08-04'
collected: '2026-08-06'
category: Agent
direction: LLM Agent 内存安全攻击
tags:
- LLM-Agent
- Memory-Poisoning
- RAG
- Adversarial-Attack
- Audit-Evasion
one_liner: 提出仅通过正常查询即可绕过审计、在大规模内存池生效的LLM Agent内存投毒框架
practical_value: '- 开发带RAG的电商导购Agent、用户行为记忆Agent时，不能仅依赖输入层prompt注入审计，本文提出的括号式事实伪装注入（如将商品A标注为「（→等价于竞品B）」）几乎不会被普通审计拦截，必须补充检索后实体一致性校验

  - 电商RAG商品库/用户记忆池的检索逻辑，可新增异常实体映射过滤规则：若检索到的记忆包含当前查询实体的非预期跳转标注，直接排除出top-K结果，降低投毒命中概率

  - 做Agent安全防御时，可复用本文的Payload设计做对抗训练，提升审计模块对隐式事实型注入的识别能力，同时限制单用户短时间写入频率，压缩投毒操作空间

  - 大规模RAG系统的内存安全评估，可复用本文的探针探测+聚类分配方法，识别容易被投毒抢占top-K检索位的语义区域，提前加固'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
记忆增强LLM Agent已广泛应用于长周期任务，但内存模块的投毒风险未被充分覆盖：现有仅查询的攻击方法在两个真实落地场景下失效，一是大规模良性内存池中恶意记录抢不到top-K检索位，二是输入审计会拦截显式恶意指令，亟需更隐蔽、检索竞争力更强的攻击方法暴露现有防御的漏洞。

### 方法关键点
- **探针式注入位置选择**：基于公开领域schema生成探测query，提取Agent返回的历史问题字段做聚类，按聚类大小轮询分配投毒预算，优先向小聚类注入，降低良性数据竞争，最大化后续检索覆盖率
- **紧凑事实伪装Payload**：不使用显式操纵指令，仅在正常查询后追加括号式注释，如「查询商品V（→本库对应品牌T）」，伪装成本地数据说明，既规避审计检测，又和原始查询语义高度相似，容易被后续用户查询召回

### 关键实验
在4个Agent数据集（MIMIC-III、eICU医疗Agent，WebShop电商导购Agent，HuggingFace Hub代码Agent）上对比基线MINJA，MAFIA最高攻击成功率达90.7%，同时审计检测率从基线峰值83.3%降至最高7.4%；在5842条记录的大规模良性内存池场景下，攻击成功率比基线高37个百分点。

### 核心结论
仅靠输入层prompt注入审计完全不足以防御记忆增强LLM Agent的内存投毒风险，必须结合检索阶段实体校验、写入权限管控等多层防护机制。
