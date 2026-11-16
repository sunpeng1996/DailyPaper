---
title: 'What a Memory Preview Cannot Tell You: Ambiguity in AI Memory Permissions'
title_zh: AI记忆权限的模糊性：内存预览无法传递的信息
authors:
- Sadia Noman Tonni
- Nafis Fuad Shahid
affiliations:
- United International University
- Islamic University of Technology
arxiv_id: '2611.17874'
url: https://arxiv.org/abs/2611.17874
pdf_url: https://arxiv.org/pdf/2611.17874
published: '2026-11-13'
collected: '2026-11-16'
category: Agent
direction: Agent 记忆权限规则歧义消除
tags:
- Conversational Memory
- Policy Authoring
- Agent Memory
- Access Control
- Usability
one_liner: 量化AI Agent内存规则预览的歧义程度，给出消除歧义所需的最小测试用例数量
practical_value: '- 开发带长期记忆的电商导购Agent时，不要依赖默认1正1负的规则预览校验权限，需新增跨任务转移测试用例，避免用户消费记忆被跨场景滥用导致推荐越界

  - 用户自定义记忆规则时可采用自适应测试策略，仅需3-4个用例即可精准匹配用户真实权限需求，比固定6-9项的检查清单交互成本低50%以上

  - 记忆规则的任务边界判断不要仅依赖文本嵌入相似度，优先让用户显式确认任务ID，可避免90%以上的跨任务权限误判'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
带记忆的LLM Agent普遍采用1个允许、1个阻止的用例预览让用户确认记忆规则，但这类预览存在严重歧义，用户实际期望的规则与系统执行的规则偏差大，极易引发隐私泄露、推荐越界等问题，在电商导购、个性化推荐等场景下风险尤其突出。

### 方法关键点
- 定义包含召回权限、推荐范围、偏好使用权限三个维度的记忆规则体系，单事件对应6种（一次性选择）或12种（显式偏好）有效规则
- 设计最大熵自适应测试、跨任务转移测试两种用例选择策略，枚举所有与当前预览兼容的规则集合，计算区分规则所需的最少测试用例
- 对比固定检查清单、自适应测试、转移测试三种策略的歧义消除效率

### 关键实验
- 枚举测试显示默认1正1负预览中92%（36/39）的负例是所有规则都阻止的无效用例，无法消除任何歧义，平均剩余3.2条兼容规则
- 3-4个精心设计的测试用例即可唯一确定规则，权限存在依赖时自适应测试最多需5-7个，远少于固定检查清单的6-9个
- 20人试点显示，看过弱预览的用户中有50%对规则的实际执行结果预测错误或不确定，且100%的预测错误用户不认可最终执行结果

### 核心结论
记忆规则预览的核心价值不是验证代码实现正确，而是区分所有用户可能存在的规则理解，无区分度的对比用例对消除歧义毫无作用
