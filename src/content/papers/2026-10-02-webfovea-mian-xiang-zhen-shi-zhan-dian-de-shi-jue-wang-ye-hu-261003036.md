---
title: 'WebFovea: When the Model Is Right but the Click Is Wrong -- Reliable Round
  Trips for Vision-Based Web Agents on Live Websites'
title_zh: WebFovea：面向真实站点的视觉网页Agent可靠交互往返框架
authors:
- Jiangang Han
affiliations:
- Independent Researcher
arxiv_id: '2610.03036'
url: https://arxiv.org/abs/2610.03036
pdf_url: https://arxiv.org/pdf/2610.03036
published: '2026-10-02'
collected: '2026-10-05'
category: Agent
direction: 网页Agent · 多模态交互可靠性优化
tags:
- WebAgent
- Multimodal
- HarnessOptimization
- Grounding
- Benchmark
one_liner: 提出四阶段交互校验框架优化视觉网页Agent，获2026 WebRetriever挑战赛第二名
practical_value: '- 做网页交互类Agent（如电商竞品爬价、用户反馈自动收集、商家后台自动操作）时，优先按「解析→执行→反馈→观测」四阶段排查错误，80%的故障大概率出在中间层而非模型推理

  - 像素点击类多模态Agent可直接复用坐标对齐方案：先校验多模态API的图片缩放比例，提前对齐截图分辨率与实际视口坐标，实测能降低70%以上的点击偏移错误

  - 所有Agent的动作限制、预算控制直接在执行层硬编码，不要只写在prompt里：比如禁止直接跳转URL、限制每类动作调用次数，能避免违规操作还能降低Token浪费

  - 负向优化参考：单独给模型加动作失败反馈提示不会改变模型重复无效动作的行为，必须搭配执行层的步数/重试预算硬限制，才能终止死循环'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
视觉网页Agent在真实站点执行信息检索、交互任务时，大量看似模型推理错误的失败（如点击空白、重复输入、放弃有效操作），实际源于模型与浏览器之间的中间层（harness）故障，现有研究大多聚焦模型本身优化，忽略了交互全链路的可靠性，导致在真实站点落地时性能远低于测试集表现。

### 方法关键点
- 每轮交互拆分为四阶段往返链路：解析（准确提取模型输出的动作，过滤自生成的聊天模板Token、截断伪造的多步轨迹）→执行（坐标对齐解决点击偏移，新增iframe DOM fallback、原生下拉框操作、输入自动校验等复合动作）→反馈（基于DOM指纹+子帧校验返回真实动作效果，避免无响应动作误导模型）→观测（新增hover、find_text、read_text工具，确保模型能获取悬停提示、长页内容、混淆字体等隐藏信息）
- 全链路加防护栏：关闭直接跳转URL、调用第三方接口等违规动作入口，所有动作预算在执行层硬编码，自动重试模型调用、页面加载错误

### 关键结果
- 全程使用固定claude-opus-4-6模型，仅优化中间层，在2026 WebRetriever挑战赛隐藏测试集得分从31.0提升至57.0，获第二名，无人工审核扣分
- 坐标对齐优化在24个开发任务上成功率从33.3%提升至83.3%，步骤超时率从67%降至4%
- 解析层Token清理修复了4.9%的被污染任务实例

**最值得记住的结论**：视觉网页Agent失败时，先别归因于模型推理能力，先检查它的决策有没有真正落地到页面，页面的响应有没有真正传回给模型。
