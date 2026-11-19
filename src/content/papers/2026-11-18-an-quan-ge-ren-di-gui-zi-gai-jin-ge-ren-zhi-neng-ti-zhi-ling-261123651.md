---
title: 'Safe Personal RSI: Evaluating and Repairing Personal-Agent Updates'
title_zh: 安全个人递归自改进：个人智能体指令更新的评估与修复方法
authors:
- Jiapeng Pei
- Yuhang Yao
- Sitan Liu
- Hanxin Chen
- Hao Li
- Guogeng Li
- Jiapei Liu
- Ruijie Chen
- Hongshan Lin
- Yang Mo
affiliations:
- Carnegie Mellon University
- University of California, San Diego
- The University of Hong Kong
- McGill University
- University of California, Berkeley
arxiv_id: '2611.23651'
url: https://arxiv.org/abs/2611.23651
pdf_url: https://arxiv.org/pdf/2611.23651
published: '2026-11-18'
collected: '2026-11-19'
category: Agent
direction: Agent 安全 · 递归自改进指令更新
tags:
- Agent Safety
- Recursive Self-Improvement
- Prompt Update
- LLM Agent
- Security Evaluation
one_liner: 提出仅修改prompt的安全RSI框架，检测修复个人智能体更新风险，拒绝20/21次高风险更新尝试
practical_value: '- 电商导购Agent、用户个人助理的prompt迭代可复用这套「新旧prompt对比测试→失败用例回滚定位→修复后验证→不达标保留旧版本」的流程，避免更新后出现隐私泄露、私自承诺优惠等违规问题

  - Agent安全评估可复用指标设计：同时统计攻击违规率和安全任务完成率，避免只看安全导致过度拒答影响用户体验，还可加入工具成本、延迟、确认请求次数的penalty做效用综合评估

  - 跨模型迁移prompt修复方案可复用：小参数模型上验证通过的安全修复prompt可直接迁移到同系列大参数模型，Qwen系列验证可降违规率从69%到17.9%，减少大模型调优成本

  - 个人Agent的runtime安全校验需独立：prompt层面的安全控制不能替代runtime的OAuth权限校验、内存持久化删除校验，避免删除的用户隐私数据被重新提取、越权调用工具'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
个人智能体（健康助理、电商导购等）的prompt迭代会提升任务处理能力，但也可能引入隐私泄露、未授权操作、谎报执行结果等风险，现有递归自改进（RSI）方案缺乏针对指令更新的标准化安全校验流程，错误更新上线会直接损害用户权益。

### 方法关键点
- 限制RSI仅修改prompt块，模型权重、runtime代码、工具实现固定，缩小更新风险边界
- 6步更新流程：提出指令修改→新旧版本对比测试失败用例→回滚变更定位问题点→针对性修复prompt→校验安全+效用+执行完整性→通过则更新否则保留旧版本
- 定义5类违规：未授权披露、隐私过度共享、误导性执行报告、未授权承诺、来源混淆；效用指标加入工具成本、延迟、确认请求的惩罚项
- 支持两种修复方式：追加分类安全规则，或用LLM基于失败trace重写prompt块，最多允许2次修复

### 关键实验
测试集含29个真实场景用例（23个邮件攻击、6个日历/健康/电商交易场景），对比基线为初始prompt、固定手写安全规则prompt、直接采用风险更新的方案。核心结果：
1. 3个模型+2种高风险更新场景下，框架拒绝20/21次更新尝试
2. GPT-5.6 Luna修复后攻击违规率从10.7%降至0%，安全任务完成率从89.7%升至100%
3. Qwen2.5-7B上训练的修复prompt迁移到Qwen3-14B，强攻击下违规率从69.0%降至17.9%，安全完成率从19.5%升至64.4%

### 核心结论
智能体prompt更新的安全校验必须和runtime的权限控制、内存校验分开做，未通过全流程验证的更新要坚决回滚到旧版本，避免盲目上线带来的安全风险。
