---
title: 'Interaction Scaling: Grounding the Third Axis of Test-Time Compute'
title_zh: 交互缩放：锚定测试时算力的第三条核心轴
authors:
- Bojie Li
- Noah Shi
affiliations:
- Pine AI
- University of Washington
arxiv_id: '2607.11598'
url: https://arxiv.org/abs/2607.11598
pdf_url: https://arxiv.org/pdf/2607.11598
published: '2026-07-13'
collected: '2026-07-14'
category: Agent
direction: Agent 测试时算力交互缩放优化
tags:
- Test-Time Compute
- Grounded Feedback
- Proposer-Reviewer
- LLM Agent
- Inference Optimization
one_liner: 提出测试时算力第三条交互轴，明确双端接地要求，突破内部推理与采样的性能上限
practical_value: '- 做Agent迭代不要盲目加循环，必须给反馈通路配覆盖业务核心缺陷的接地工具：比如生成电商落地页时直接测量DOM布局缺陷，不要用VLM读截图判断效果，避免无效优化

  - 代码/营销文案/素材生成类Agent可直接复用proposer-reviewer架构，用执行/测量工具的结构化结果驱动修订，比纯LLM自我批评成本低2.5倍，效果更稳定

  - 做效果评估时必须用接地的客观指标：比如推荐素材的布局合规性、商品详情页的功能正确性直接读渲染后的真实参数/执行结果，不要用VLM/人工主观打分，否则会漏掉核心缺陷，无法正确衡量迭代收益

  - 小模型部署可蒸馏大模型在接地交互环里的优质轨迹，能以1/10成本恢复大模型70%的能力，适合业务侧降本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前测试时算力优化仅有推理缩放（CoT、思维树）和采样缩放（best-of-N）两类，二者都是基于固定权重和prompt的内部信息重组，存在天然性能天花板；且传统基于模型打分的评估方式存在结构性盲区，无法准确衡量迭代效果，亟需明确第三条优化路径的落地标准。

### 方法关键点
- 定义**交互缩放**为测试时算力的第三轴：通过外部工具观测生成artifact的真实状态，驱动模型迭代修订，引入外部信息突破内部天花板
- 提出双端接地要求：反馈信号必须来自观测真实缺陷的工具（如执行pytest、测量DOM布局），评估指标也必须基于相同接地观测，避免信号损失
- 设计无微调的proposer-reviewer架构：冻结LLM分别承担生成和缺陷解析角色，基于工具输出的结构化缺陷列表迭代，保留最优版本
- 提出覆盖度原则：接地工具的观测范围决定收益上限，仅能观测表面特征的工具（如linter）无法修复逻辑类缺陷，截图输入的VLM存在布局盲区

### 关键结果
- 代码生成任务：相同token预算下，内部推理/采样分别饱和在73.3%、86.7%通过率，接地交互方案达到100%通过率，token成本比其他交互方案低28%，且跨Claude、Qwen3、GPT-5三类模型均有效
- 视觉布局任务：VLM读截图的评估方式会将14/15的破损布局判定为完美，基于DOM测量的接地评估可检测到全部缺陷，接地反馈可降低40%-74%的布局缺陷，而VLM作为反馈源反而会使布局缺陷增加
- 小模型蒸馏：8B小模型蒸馏大模型交互轨迹后，以1/10部署成本恢复大模型70%的能力

### 最值得记住的一句话
不要盲目给Agent加循环，要先把反馈和评估的通路接地，用能观测到真实缺陷的工具驱动迭代，否则再多算力投入也看不到实质收益
