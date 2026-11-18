---
title: 'When Passing Checks Do Not Establish Completion: Evidence Interpretation in
  Coding Agents'
title_zh: 编码Agent验证证据解释研究：通过检查不代表任务完成
authors:
- Xueping Gao
affiliations:
- Alibaba Cloud Computing
arxiv_id: '2611.22835'
url: https://arxiv.org/abs/2611.22835
pdf_url: https://arxiv.org/pdf/2611.22835
published: '2026-11-17'
collected: '2026-11-18'
category: Agent
direction: Agent 编码任务验证逻辑优化
tags:
- Coding Agent
- Verification
- Evidence Interpretation
- Program Repair
- LLM Agent
one_liner: 实证揭示编码Agent验证通过不代表任务完成，明确证据解释的边界与依赖
practical_value: '- 面向自研业务Agent（如推荐规则生成Agent、运维Agent）的验证环节，可引入证据四要素校验规则：绑定目标操作、执行上下文、时间窗口、前置条件，避免仅靠布尔结果判断完成，降低上线假阳性风险

  - 针对Agent生成的代码/规则的回归测试，可采用分层验证逻辑：先做执行可达性校验，再做目标操作有效性校验，最后做兼容性校验，覆盖更多隐式缺陷

  - 对于依赖外部工具返回结果的Agent（如RAG Agent、API调用Agent），不能直接信任工具返回的成功标识，需额外校验返回证据是否匹配请求目标、覆盖授权范围，避免错误结论'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有编码Agent的验证流程通常仅通过检查是否通过判定任务完成，但生产环境中代码修改可能影响验证流程本身的执行逻辑，导致通过验证的修改实际未完成目标甚至引入新缺陷，当前缺乏对这一问题的系统性实证分析。

### 方法关键点
- 设计分层证据表示框架，将验证证据拆分为源摘要、检查项、执行阶段、目标操作、记录凭证5个维度，明确证据的适用范围
- 采用源码干预的因果分析方法，通过组件回滚、上下文替换、生命周期控制等手段，分离验证结果的真实来源
- 覆盖31个真实开源仓库任务、118次修复流程，对比Qwen3-Coder-30B、Devstral Small 2 24B两个编码大模型的表现

### 关键结果数字
- 收据供应实验中122个返回的验证标签全部正确，但仅95/128的输出满足事实+范围的联合要求，16个存在事实错误，11个超出授权范围
- 验证通过的修复中存在大量假阳性：flush修复场景下两个模型的修复都通过了官方检查，但Qwen的修复实际未实现目标显式刷新逻辑，还引入了兼容性问题
- 生成的解释与修复成功率无关：即使修复成功，生成的诊断解释仍可能存在事实错误，额外的解释引导未带来一致的修复效果提升

### 核心结论
Agent的验证结论必须绑定实际执行的操作与时间窗口，不能仅依赖布尔型的通过标识，修复效果需要与解释正确性分开评估
