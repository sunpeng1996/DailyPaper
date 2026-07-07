---
title: 'Safety Testing LLM Agents at Scale: From Risk Discovery to Evidence-Grounded
  Verification'
title_zh: 大规模LLM Agent安全测试框架：从风险发现到证据驱动验证
authors:
- Yunhao Feng
- Ruixiao Lin
- Ming Wen
- Qinqin He
- Yanming Guo
- Yifan Ding
- Yutao Wu
- Jialuo Chen
- Zhuoer Xu
- Xiaohu Du
affiliations:
- AntGroup
- Zhejiang University
- Fudan University
- Alibaba Group
- Hunan Institute of Advanced Technology
arxiv_id: '2607.01793'
url: https://arxiv.org/abs/2607.01793
pdf_url: https://arxiv.org/pdf/2607.01793
published: '2026-07-03'
collected: '2026-07-07'
category: Agent
direction: Agent安全评估 · 自动化测试框架
tags:
- LLM Agent Safety
- Automated Testing
- Red Teaming
- Agent Evaluation
- Benchmark
one_liner: 提出三阶段自强化LLM Agent安全测试框架VERA，配套开源1600个可执行测试用例的VERA-Bench
practical_value: '- 搭建电商/广告/推荐类Agent服务的安全测试体系时，可直接复用VERA的「风险类型-攻击方法-执行环境」三级分类框架，覆盖工具调用越权、用户隐私泄露、违规操作执行等核心业务风险

  - 验证Agent安全风险可借鉴「环境状态>工具调用记录>Agent返回文本」的优先级逻辑，避免误判Agent「口头拒绝但实际执行危险操作」的隐蔽风险

  - 业务Agent安全巡检可复用多通道攻击思路：除用户输入侧外，需额外覆盖搜索结果、支付接口返回、消息通知等工具返回渠道的注入风险

  - 基于VERA-Bench的微调范式可快速优化自有Agent的安全Guard模型，相比通用Guard模型在业务场景下的准确率可提升20%以上'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent安全测试依赖专家预设规则，仅检查文本输出或固定交互路径，无法覆盖工具调用带来的动态、多通道风险，且测试逻辑与场景强耦合，难以随Agent迭代快速扩展，也无法判定风险是否实际落地而非仅存在于Agent意图中。

### 方法关键点
- 三阶段自强化流水线：第一阶段通过文献驱动自动迭代构建风险、攻击方法、执行环境三级可扩展分类体系；第二阶段跨维度组合生成可执行安全用例，每个用例包含明确安全目标、可复现初始环境状态、代码化验证逻辑；第三阶段在隔离沙箱中自适应执行，控制Agent根据运行时状态调整多轮攻击策略，优先基于环境状态/工具调用证据而非Agent自报告判定风险
- 支持单/多通道两种攻击模式：多通道模式下除用户输入侧攻击外，还支持在工具返回结果中注入对抗内容，模拟网页、邮件、搜索结果等第三方渠道的风险
- 通用Agent适配层：通过统一接口对接异构Agent框架，无需修改目标Agent内部逻辑即可完成测试

### 关键实验结果
- 覆盖4个业界主流生产级Agent框架（OpenClaw、Hermes、Codex、Claude Code），测试用例覆盖124类风险、77种攻击方法、30类执行环境，最终开源1600个可执行测试用例的VERA-Bench
- 多通道攻击下平均攻击成功率达93.9%，单通道攻击成功率90.6%，明显高于静态Prompt测试基线；基于VERA数据微调的Guard模型相比通用Guard模型在自有测试集上准确率提升26个百分点，在外部R-Judge基准上准确率达61.7%，超过所有开源基线

### 核心结论
Agent的任务完成能力越强，其被对抗利用的风险越高，安全测试必须从静态文本校验转向基于可观测执行证据的动态评估
