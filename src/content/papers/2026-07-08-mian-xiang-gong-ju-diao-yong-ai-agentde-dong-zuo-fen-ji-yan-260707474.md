---
title: 'Beyond Attack-Success Rate: Action-Graded Severity Scale for Tool-Using AI
  Agents'
title_zh: 面向工具调用AI Agent的动作分级严重程度评估体系
authors:
- Harry Owiredu-Ashley
affiliations:
- Independent Researcher, New Jersey, USA
arxiv_id: '2607.07474'
url: https://arxiv.org/abs/2607.07474
pdf_url: https://arxiv.org/pdf/2607.07474
published: '2026-07-08'
collected: '2026-07-09'
category: Agent
direction: Agent安全评估·攻击严重度分级
tags:
- Agent Safety
- Red Teaming
- LLM-as-Judge
- Prompt Injection
- Severity Scoring
one_liner: 提出基于动作后果的7级严重度分级体系，替代二进制攻击成功率评估Agent安全风险
practical_value: '- 电商/广告Agent（客服、导购、运营类）做安全评估时，可直接复用7级严重度框架（可逆性/跨域/权限提升三个维度）分级评估风险，优先修复高等级漏洞

  - 评估Agent防御手段效果时，不能仅看攻击成功率下降幅度，需同时监控L5/L6等高严重度尾部分布，避免出现「成功率降低但漏防的攻击更危险」的反效果

  - 无程序化检测能力的场景，可复用论文的LLM-judge分级prompt设计，当前前沿模型做该任务的Krippendorff''s α可达0.91，仅需补充升级链识别逻辑即可落地

  - 做Agent工具权限管控时，可参考工具元数据标注方法，提前标记每个工具的可逆性、跨域属性、权限属性，在运行时做风险拦截'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Agent红队评估仅使用二进制攻击成功率（ASR）作为核心指标，完全丢失了攻击实际造成的后果严重度信息：既无法区分同样攻击成功下的不同危害程度，还会出现「防御手段ASR为0但实际仍存在跨域信息泄露」的误导性结果，无法支撑业务上线前的风险决策。
### 方法关键点
- 设计7级（L0-L6）序数严重度分级框架，核心依据三个动作后果维度：动作是否可逆、是否跨用户/跨域触达第三方、是否提升权限，L6专门标记多步攻击升级链
- 两种分级实现：① 程序化Oracle：基于预定义的工具元数据（每个工具的可逆性、权限属性）+ 攻击目标参数匹配规则，直接从执行轨迹计算等级，不依赖基准的ASR结果；② 3个前沿LLM组成的评审团，仅输入无标签的执行轨迹描述和分级规则，独立输出等级
- 归因规则仅匹配攻击者目标的关键参数（如目标邮箱、目标文件ID），不依赖基准的攻击成功判定，可跨环境迁移
### 关键结果
在AgentDojo工作区套件上测试，覆盖4个受害模型、2种防御、共410个episode，188个样本用于LLM评审团评估：① 某工具过滤防御ASR从40%降到0，但仍有2%的攻击达到L4跨域泄露等级；② spotlighting防御将ASR从48%降到40%，但L5/L6高严重度攻击从1例升至3例；③ LLM评审团和Oracle的序数一致性Krippendorff's α达0.91，精确匹配率超85%，但普遍无法识别L6升级链。
> 最值得记住：Agent安全评估不能只看攻击是否成功，要基于实际执行动作的后果分级，二进制指标经常误导上线决策。
