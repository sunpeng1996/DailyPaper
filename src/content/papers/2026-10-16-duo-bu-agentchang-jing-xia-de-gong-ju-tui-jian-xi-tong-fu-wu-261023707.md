---
title: 'Tool Recommendation for Multi-Step Agents: Finding Every Tool a Task Needs'
title_zh: 多步Agent场景下的工具推荐系统：覆盖任务所需全部工具
authors:
- Sam Partee
- River Stevens
- Thierry Damiba
- Valerie Fanelle
affiliations:
- Arcade.dev
arxiv_id: '2610.23707'
url: https://arxiv.org/abs/2610.23707
pdf_url: https://arxiv.org/pdf/2610.23707
published: '2026-10-16'
collected: '2026-10-19'
category: Agent
direction: Agent 工具调用优化 · 工具推荐
tags:
- Tool Recommendation
- LLM Agent
- MCP
- Retrieval
- Cost Optimization
one_liner: 部署级两阶段工具推荐系统，通过3个固定元工具实现万级工具库低耗高召回访问
practical_value: '- 多步依赖类任务的工具/服务召回优先用Completeness@K指标替代单纯Recall@K，只要缺一个工具就会导致全链路失败，电商Agent多步运营、客服类场景可直接复用该指标逻辑

  - 两阶段检索架构可直接迁移到大规模工具/API/服务召回场景：第一阶段BM25+稠密检索加权融合做召回，第二阶段小参数量（1.2B）交叉编码器做重排，性能可比肩9倍参数量的大模型，推理延迟仅百毫秒级

  - 成本优化不要只看输入token减少比例，要结合厂商实际计费规则（比如KV cache折扣、输出token定价）测算真实账单成本，论文中17%~40%的token减少仅对应5.5%~21.8%的账单降低

  - 静态工具列表与动态推荐的取舍阈值可直接复用：工具数<25~28个、单步短任务用静态列表更划算；多步长任务、工具库规模超过30个时用动态推荐成本更低覆盖更全'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
多步Agent的任务只要缺失一个所需工具就会全链路失败，但企业级工具库往往有数千到上万款工具，全量工具定义塞入上下文会远超模型窗口，还会大幅提升调用成本；静态工具列表覆盖范围有限，微调模型又跟不上工具库的每日更新，亟需兼顾召回准确率、覆盖度和成本的工具调度方案。

### 方法关键点
- 接口层仅暴露3个固定元工具（SelectTools/UseTool/ListApps），总定义仅993 tokens，比1.76M tokens的全量8200个工具定义小1800倍，兼容MCP协议所有客户端
- 推荐链路采用两阶段排序：第一阶段融合BM25与稠密检索召回候选集，第二阶段用1.2B参数量交叉编码器重排，生产环境中位数响应131ms，95分位292ms
- 权限管控全在网关层执行，所有工具调用使用用户自身授权，凭证不进入Agent上下文，避免权限泄露

### 关键实验
在公开ToolRet基准（7961条查询、44453个工具）上测试，Completeness@10达45.2%，比商用工具搜索常用的BM25高57%，性能优于6~9倍参数量的公开竞品；端到端测试中93%的Codex多步会话首次推荐就覆盖全部所需工具；对比100个工具的静态列表，Codex输入token降17%、总账单降5.5%，Claude Code输入token降40%、总账单降21.8%，14组对照测试全部成本更低，且任务完成率无差异。

**最值得记住的一句话**：动态工具推荐在工具库大于25~28个的多步Agent场景下，不仅能覆盖全量工具能力，实际调用成本反而低于固定长度的静态工具列表。
